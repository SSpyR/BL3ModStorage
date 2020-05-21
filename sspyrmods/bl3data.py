#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# Borderlands 3 Data Library is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# Borderlands 3 Data Library is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Borderlands 3 Data Library.  If not, see
# <https://www.gnu.org/licenses/>.

import os
import re
import json
import glob
import appdirs
import MySQLdb
import subprocess
import configparser

from bl3hotfixmod import BVC

class BL3Data(object):
    """
    Class to assist in programmatically inspecting Borderlands 3 data as much as
    possible.  The first time this class is instantiated, it'll create a config
    file and then error out.  To use the class, populate at least the "filesystem"
    section of the config file (the path will be provided on the console).

    The "filesystem" section contains two config values:

        1) data_dir - This is a directory containing data extracted from the BL3
           .pak files using UnrealPak.  It should also be processed so that the
           pathnames on the filesystem match the object names exactly.

        2) ueserialize_path - This is the path to a 'ueserialize' binary from the
           JohnWickParse project, used to serialize borderlands .uasset/.umap files
           to a JSON object.  This is what's used to process the extracted data into
           a format we can work with, on an on-demand basis.

           I'm using a custom fork of this which adds some versioning information to
           the generated JSON, so that I can leave serializations on-disk but "force"
           them to re-generate when there are patches, in case the data's been updated.
           (My fork also includes various other bits of information which are useful
           to a would-be BL3 modder, like it prints out the indexes of all the arrays,
           etc, and puts in some extra info when objects reference other exports within
           the object.)

           If you don't use my fork, you'll end up serializing the same data over and
           over.  If you use the "vanilla" JWP version, you'll probably want to search
           for `BL3Data.data_version` down in the code, in `get_data()`, and remove
           that check from the code.  (And then manually clear out the `.json` files
           when you suspect that an object needs re-serialization.)  Otherwise, just
           compile up my fork/branch and use that.  Make sure you're using the
           `indexed_arrays` branch in particular, on my own fork.

           Vanilla JWP: https://github.com/SirWaddles/JohnWickParse
           My fork/branch: https://github.com/apocalyptech/JohnWickParse/tree/indexed_arrays

    The "database" section contains the values "host", "db", "user", and "passwd".
    These define the connection parameters to a MySQL database populated with BL3
    reference data, which can be found at: http://apocalyptech.com/games/bl3-refs/
    This is only required if you want to use the `get_refs_to()` or `get_refs_from()`
    methods of this class, and BL3Data will not attempt any database connections
    until either of those methods are called.
    """

    # Data serialization version requirements
    data_version = 7

    # Hardcoded BVA values
    bva_values = {
            }

    # Hardcoded part-category values
    cats_shields = [
            'BODY',
            'RARITY',
            'LEGENDARY AUG',
            'AUGMENT',
            'ELEMENT',
            'MATERIAL',
            ]

    cats_grenades = [
            'MANUFACTURER',
            'ELEMENT',
            'RARITY',
            'AUGMENT',
            'BEHAVIOR',
            'MATERIAL',
            ]

    cats_coms = [
            'CHARACTER',
            'MODTYPE',
            'RARITY',
            'PRIMARY',
            'SECONDARY',
            'SKILLS',
            '(unknown)',
            ]

    cats_artifacts = [
            'RARITY',
            'LEGENDARY ABILITY',
            'ABILITY',
            'PRIMARY',
            'SECONDARY',
            ]

    def __init__(self):
        """
        Initialize a BL3Data object.  Will create a sample config file if one
        is not already found.  Will require that the "filesystem" section be
        properly filled in, or we'll raise an exception.
        """

        config_dir = appdirs.user_config_dir('bl3data')

        # Create the config dir if it doesn't exist
        if not os.path.exists(config_dir):
            os.makedirs(config_dir, exist_ok=True)

        # Create a sample INI file it if doesn't exist
        self.config_file = os.path.join(config_dir, 'bl3data.ini')
        if not os.path.exists(self.config_file):
            config = configparser.ConfigParser()
            config['filesystem'] = {
                    'data_dir': 'C:/Users/lavoiet2/Downloads/BL3/StandaloneHotfixInjection/HotfixModdingResources/BL3Data',
                    'ueserialize_path': 'C:/Users/lavoiet2/Downloads/BL3/Datamining/parser/john-wick-parse.exe',
                    }
            config['mysql'] = {
                    'host': 'CHANGEME',
                    'db': 'CHANGEME',
                    'user': 'CHANGEME',
                    'passwd': 'CHANGEME',
                    }
            with open(self.config_file, 'w') as odf:
                config.write(odf)
            print('Created sample config file {}'.format(self.config_file))

        # Read in the config file and at least make sure we have filesystem
        # data available
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        self._enforce_config_section('filesystem')

        # Convenience var
        self.data_dir = self.config['filesystem']['data_dir']

        # Now the rest of the vars we'll use
        self.cache = {}
        self.balance_to_extra_anoints = None
        self.db = None
        self.curs = None

    def _enforce_config_section(self, section_name):
        """
        Raises an exception if the configuration section `section_name` hasn't
        been changed from its "CHANGEME" defaults.
        """
        if any([v == 'CHANGEME' for v in self.config[section_name].values()]):
            raise Exception('Populate the "{}" section in {} to continue'.format(
                section_name,
                self.config_file,
                ))

    def _connect_db(self):
        """
        Attempts to connect to the refs database, if we haven't already done so.
        """
        if self.db is None:
            self._enforce_config_section('mysql')
            self.db = MySQLdb.connect(
                    user=self.config['mysql']['user'],
                    passwd=self.config['mysql']['passwd'],
                    host=self.config['mysql']['host'],
                    db=self.config['mysql']['db'],
                    )
            self.curs = self.db.cursor()

    def get_data(self, obj_name):
        """
        Returns a JSON-serialized version of the object `obj_name`, if possible.
        May return None, either due to the object not existing, or if JohnWickParse
        can't actually produce a serialization for the object.  Results will be
        cached, so requesting the same object more than once will not result in
        re-parsing JSON content.
        """
        if obj_name not in self.cache:

            base_path = '{}{}'.format(self.data_dir, obj_name)
            json_file = '{}.json'.format(base_path)
            print(json_file)
            if not os.path.exists(json_file):
                # PyPy3 is still on 3.6, which doesn't have capture_output
                #subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', capture_output=True)
                subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if os.path.exists(json_file):
                with open(json_file) as df:
                    self.cache[obj_name] = json.load(df)
                if len(self.cache[obj_name]) > 0:
                    if '_apoc_data_ver' not in self.cache[obj_name][0] or self.cache[obj_name][0]['_apoc_data_ver'] < BL3Data.data_version:
                        # Regenerate if we have an old serialization
                        subprocess.run([self.config['filesystem']['ueserialize_path'], base_path], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        with open(json_file) as df:
                            self.cache[obj_name] = json.load(df)
            else:
                self.cache[obj_name] = None

        return self.cache[obj_name]

    def find(self, base, prefix):
        """
        Given a base object path `base`, recursively search through to find any
        objects with the prefix `prefix`.  Will match case-insensitively.  Will
        yield the object names as they're found.
        """
        prefix_lower = prefix.lower()
        base_dir = '{}{}'.format(self.data_dir, base)
        results = []
        for (dirpath, dirnames, filenames) in os.walk(base_dir):
            obj_base = dirpath[len(self.data_dir):]
            for filename in filenames:
                if filename.lower().startswith(prefix_lower) and filename.endswith('.uasset'):
                    yield os.path.join(obj_base, filename[:-7])

    def find_data(self, base, prefix):
        """
        Given a base object path `base`, recursively search through to find any
        objects with the prefix `prefix`.  Will match case-insensitively.  Will
        yield the JSON-serialized data of the objects (or None, if no serialization
        is possible) as they're found.
        """
        for obj_name in self.find(base, prefix):
            yield (obj_name, self.get_data(obj_name))

    def glob(self, glob_pattern):
        """
        Find classes which match the given `glob_pattern` and yield the
        object names which were found.
        https://en.wikipedia.org/wiki/Glob_(programming)
        """
        for filename in glob.glob('{}{}'.format(self.data_dir, glob_pattern)):
            if filename.endswith('.uasset'):
                yield filename[len(self.data_dir):-7]

    def glob_data(self, glob_pattern):
        """
        Find classes which match the given `glob_pattern` and yield the
        serialized object data for each (or None if unavailable).
        https://en.wikipedia.org/wiki/Glob_(programming)
        """
        for obj_name in self.glob(glob_pattern):
            yield (obj_name, self.get_data(obj_name))

    def get_export_idx(self, obj_name, export_idx):
        """
        Given an object `obj_name`, return the specified export at `export_idx`, or
        None.
        """
        if export_idx == 0:
            return None
        data = self.get_data(obj_name)
        if export_idx > len(data):
            return None
        else:
            return data[export_idx-1]

    def get_exports(self, obj_name, export_type):
        """
        Given an object `obj_name`, return a list of serialized exports which match
        the type `export_type`.
        """
        exports = []
        data = self.get_data(obj_name)
        if data:
            for export in data:
                if export['export_type'] == export_type:
                    exports.append(export)
        return exports

    def get_refs_to(self, obj_name):
        """
        Find all object names which reference the given `obj_name`, and return
        a list of those objects.  Requires a database connection to the refs
        database.
        """
        self._connect_db()
        self.curs.execute("""select o2.name
                from bl3object o, bl3refs r, bl3object o2
                where
                    o.name=%s
                    and o.id=r.to_obj
                    and o2.id=r.from_obj
                """, (obj_name,))
        return [row[0] for row in self.curs.fetchall()]

    def get_refs_to_data(self, obj_name):
        """
        Find all object names which reference the given `obj_name`, and yield
        tuples consisting of the object name and the serialized object data.
        Requires a database connection to the refs database.
        """
        for ref in self.get_refs_to(obj_name):
            yield (ref, self.get_data(ref))

    def get_refs_from(self, obj_name):
        """
        Find all object names which `obj_name` references, and return
        a list of those objects.  Requires a database connection to the refs
        database.
        """
        self._connect_db()
        self.curs.execute("""select o2.name
                from bl3object o, bl3refs r, bl3object o2
                where
                    o.name=%s
                    and o.id=r.from_obj
                    and o2.id=r.to_obj
                """, (obj_name,))
        return [row[0] for row in self.curs.fetchall()]

    def get_refs_from_data(self, obj_name):
        """
        Find all object names which `obj_name` references, and yield tuples
        consisting of the object name and the serialized object data.  Requires
        a database connection to the refs database.
        """
        for ref in self.get_refs_from(obj_name):
            yield (ref, self.get_data(ref))

    def get_refs_objects_by_short_name(self, short_name):
        """
        Find all objects in our references database whose "short" object
        name (ie: the last path component) is `short_name`.  Requires a
        database connection to the refs database.
        """
        self._connect_db()
        self.curs.execute('select name from bl3object where name like %s',
                (f'%/{short_name}',))
        return [row[0] for row in self.curs.fetchall()]

    def datatable_lookup(self, table_name, row_name, col_name):
        """
        Given a `table_name`, `row_name`, and `col_name`, return the specified cell.
        """
        data = self.get_exports(table_name, 'DataTable')[0]
        if row_name in data and col_name in data[row_name]:
            return data[row_name][col_name]
        else:
            return None

    def process_bvc(self, bvc_obj):
        """
        Given a bl3hotfixmod BVC object, return a value.
        """

        # BVC
        bvc = bvc_obj.bvc

        # DT
        if bvc_obj.dtv and bvc_obj.dtv.table != 'None':
            new_bvc = self.datatable_lookup(bvc_obj.dtv.table, bvc_obj.dtv.row, bvc_obj.dtv.value)
            if new_bvc is not None:
                bvc = new_bvc

        # BVA
        if bvc_obj.bva and bvc_obj.bva != 'None':
            attr_name = bvc_obj.bva
            if attr_name in self.bva_values:
                bvc = self.bva_values[attr_name]
            else:
                # Try to read the attr
                base = self.get_exports(attr_name, 'GbxAttributeData')
                if len(base) != 1:
                    raise Exception('bva: {}'.format(attr_name))
                if 'ValueResolver' not in base[0]:
                    raise Exception('bva: {}'.format(attr_name))
                lookup_export = base[0]['ValueResolver']['export']
                lookup = self.get_export_idx(attr_name, lookup_export)
                lookup_type = lookup['export_type']
                if lookup_type == 'ConstantAttributeValueResolver':
                    bvc = lookup['Value']['BaseValueConstant']
                    #print('{} -> {}'.format(attr_name, bvc))
                elif lookup_type == 'DataTableAttributeValueResolver':
                    table_name = lookup['DataTableRow']['DataTable'][1]
                    row = lookup['DataTableRow']['RowName']
                    col = lookup['Property']['ParsedPath']['PropertyName']
                    new_bvc = self.datatable_lookup(table_name, row, col)
                    if new_bvc is not None:
                        bvc = new_bvc
                    #print('{} -> {}'.format(attr_name, bvc))
                else:
                    raise Exception('Unknown bva type {} for {}'.format(lookup_type, attr_name))

        # AI
        if bvc_obj.ai and bvc_obj.ai != 'None':
            raise Exception('ai: {}'.format(data['BaseValueAttribute']))

        # BVS
        return bvc * bvc_obj.bvs

    def process_bvc_struct(self, data):
        """
        Given a serialized BVC/BVSC/etc structure, return a value.
        """

        return self.process_bvc(BVC.from_data_struct(data))

    def guess_part_category_name(self, part_name):
        """
        Given a `part_name`, try and guess what the category name is, for the parts category
        which this part lives in.  This may or may not be accurate depending on context,
        but it'll be the best we can do given the current part.  (Keep in mind that these
        category names are NOT really part of the base game data itself.  I've done a fair
        bit of tweaking so they "make sense," at least to myself.  The labels you see
        in the Item Inspector in-game are often pretty good guidelines but they're not
        always consistent.)
        """

        if not part_name:
            return None

        part_lower = part_name.lower()

        # First, a hardcode for a part that we currently can't serialize
        if part_lower == '/game/gear/grenademods/_design/partsets/part_manufacturer/gm_part_manufacturer_06_pangolin':
            return 'MANUFACTURER'

        # Grab the data itself and see if we can do anything with it.
        part_obj = self.get_data(part_name)
        for export in part_obj:
            if export['export_type'].startswith('BPInvPart_'):
                if 'PartInspectionTitleOverride' in export:
                    title_name = export['PartInspectionTitleOverride'][0][1]
                    title_obj = self.get_data(title_name)
                    ui_label = re.sub(r'\[/?.*?\]', '', title_obj[0]['Text']['string'])

                    # Some hardcoded overrides here
                    if ui_label.startswith('TRACKING '):
                        return 'TRACKING METHOD'
                    elif ui_label.endswith(' SHIELD'):
                        return 'SHIELD TYPE'
                    elif ui_label.endswith(' MODULE'):
                        return 'RELOAD TYPE'
                    elif ui_label.startswith('UNDERBARREL '):
                        return 'UNDERBARREL TYPE'
                    else:
                        return ui_label

                elif 'material' in part_lower or '_mat_' in part_lower \
                        or part_lower.endswith('_mat') \
                        or part_lower.endswith('/part_sr_dal_worlddestroyer') \
                        or part_lower.endswith('/part_sr_hyp_masterwork') \
                        or part_lower.endswith('/part_sr_hyp_zeroforplayer') \
                        or part_lower.endswith('/part_sr_hyp_tankman') \
                        or part_lower.endswith('/part_sr_jak_icequeen') \
                        or part_lower.endswith('/part_sr_hyp_woodblocks'):
                    return 'MATERIAL'

                elif 'frontsight' in part_lower:
                    return 'FRONT SIGHT'

                elif 'slidecap' in part_lower:
                    return 'CAPS'

                elif 'underbarrel' in part_lower:
                    return 'UNDERBARREL TYPE'

                elif 'magazine' in part_lower or '_mag_' in part_lower:
                    return 'MAGAZINE'

                elif 'thewave' in part_name:
                    return 'TK WAVE'

                elif '_sight_' in part_name:
                    return 'SIGHT'

                elif part_lower.endswith('_boomsickle'):
                    return 'BOOM SICKLE'

                elif part_lower.endswith('_trigger_fingerbiter') \
                        or part_lower.endswith('_trigger_hellwalker'):
                    return 'BODY ACCESSORY'

                elif part_lower.endswith('/part_ar_cov_scopemount'):
                    return 'RAIL'

                elif part_lower.endswith('/part_sg_jak_body') \
                        or part_lower.endswith('/part_ps_mal_body') \
                        or part_lower.endswith('/part_ps_vla_body'):
                    return 'BODY'

                break

        return None

    def get_parts_category_name(self, part_names, balance_name, cat_idx):
        """
        Given a list of `part_names`, figure out the most reasonable category name to
        use for those parts.  `balance_name` and `cat_idx` are used for some hardcoded
        tiebreakers, when we can't auto-determine it.
        """

        # First up: if we're NOT dealing with a weapon, we're using some hardcoded
        # values, 'cause it's super annoying otherwise
        if '/Shield/' in balance_name or '/Shields/' in balance_name:
            return self.cats_shields[cat_idx]
        elif '/GrenadeMods/' in balance_name or '/Grenade/' in balance_name:
            return self.cats_grenades[cat_idx]
        elif '/ClassMods/' in balance_name or '/CM/' in balance_name:
            return self.cats_coms[cat_idx]
        elif '/Artifacts/' in balance_name:
            return self.cats_artifacts[cat_idx]

        # Construct a sort of label histogram
        valid_labels = {}
        for part_name in part_names:
            label = self.guess_part_category_name(part_name)
            if label:
                if label in valid_labels:
                    valid_labels[label] += 1
                else:
                    valid_labels[label] = 1

        # Pick the most-used one
        label_text = None
        label_max = -1
        contention = False
        for label, count in valid_labels.items():
            if count > label_max:
                contention = False
                label_max = count
                label_text = label
            elif count == label_max:
                contention = True

        # Resolve some contentions with hard-coded values, if we can
        if contention:
            if balance_name == '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf' and cat_idx == 1:
                # BODY ACCESSORY vs. BARREL ACCESSORY
                contention = False
                label_text = 'BODY ACCESSORY'
            elif balance_name == '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre' and cat_idx == 10:
                # IRON SIGHTS vs. RAIL
                contention = False
                label_text = 'RAIL'

        # Return
        if contention:
            return None
        else:
            return label_text

    def get_extra_anoints(self, balance_name):
        """
        Given a `balance_name`, return a list of tuples, each with two elements:
          1) The GPartExpansion object providing extra anointments (or None)
          2) A list of anointments which that GPartExpansion is adding to the object.
        """

        # First, if we haven't read in the GPartExpansion data and created our lookup
        # object, do that.
        if not self.balance_to_extra_anoints:

            self.balance_to_extra_anoints = {}

            for expansion_name in [
                    '/Game/PatchDLC/Raid1/Gear/_GearExtension/GParts/GPartExpansion_Grenades_Raid1',
                    '/Game/PatchDLC/Raid1/Gear/_GearExtension/GParts/GPartExpansion_Shields_Raid1',
                    '/Game/PatchDLC/Raid1/Gear/_GearExtension/GParts/GPartExpansion_Weapons_Raid1',
                    # These objects do exist, but they don't actually add any parts, so whatever.
                    # The BloodyHarvest ones *do* add them, but only during the event, so we're ignoring
                    # those too.
                    #'/Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/GPartExpansion_Grenades_BloodyHarvest',
                    #'/Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/GPartExpansion_Shields_BloodyHarvest',
                    #'/Game/PatchDLC/BloodyHarvest/Gear/_Design/_GearExtension/GParts/GPartExpansion_Weapons_BloodyHarvest',
                    #'/Game/PatchDLC/Dandelion/Gear/_GearExtension/GParts/GPartExpansion_Grenades_Dandelion',
                    #'/Game/PatchDLC/Dandelion/Gear/_GearExtension/GParts/GPartExpansion_Shields_Dandelion',
                    #'/Game/PatchDLC/Dandelion/Gear/_GearExtension/GParts/GPartExpansion_Weapons_Dandelion',
                    #'/Game/PatchDLC/Hibiscus/Gear/_GearExtension/GParts/GPartExpansion_Grenades_Hibiscus',
                    #'/Game/PatchDLC/Hibiscus/Gear/_GearExtension/GParts/GPartExpansion_Shields_Hibiscus',
                    #'/Game/PatchDLC/Hibiscus/Gear/_GearExtension/GParts/GPartExpansion_Weapons_Hibiscus',
                    ]:

                # Construct a list of anointments which this GPartExpansion provides
                extra_anoints = []
                expansion_data = self.get_exports(expansion_name, 'InventoryGenericPartExpansionData')[0]
                for part in expansion_data['GenericParts']['Parts']:
                    extra_anoints.append(part['PartData'][1])

                # Grab a list of balance collections which define the gear this expansion acts on.
                bal_collections = [expansion_data['InventoryBalanceCollection'][1]]
                for (extra, extra_data) in self.get_refs_to_data(bal_collections[0]):
                    if extra_data \
                            and extra_data[0]['export_type'] == 'InventoryBalanceCollectionData' \
                            and extra_data[0]['ParentCollection'][1] == bal_collections[0]:
                        bal_collections.append(extra)

                # Now loop through all balances and populate our dict
                for bal_collection in bal_collections:
                    collection = self.get_exports(bal_collection, 'InventoryBalanceCollectionData')[0]
                    if 'InventoryBalanceList' in collection:
                        for bal in collection['InventoryBalanceList']:
                            this_balance = bal['asset_path_name'].split('.')[0]
                            if this_balance not in self.balance_to_extra_anoints:
                                self.balance_to_extra_anoints[this_balance] = []
                            self.balance_to_extra_anoints[this_balance].append((expansion_name, extra_anoints))

        # Now, return the appropriate value
        if balance_name in self.balance_to_extra_anoints:
            return self.balance_to_extra_anoints[balance_name]
        else:
            return []
