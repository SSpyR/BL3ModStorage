#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
import sys
from bl3data.bl3data import BL3Data
from bl3hotfixmod.bl3hotfixmod import Mod

# While doing savegame investigation, it looked like the best way to find
# the current map was to start with the fast travel station in a
# last_active_travel_station_for_playthrough string.  We'd want to map
# that back to a level, so this generates that mapping.  (I didn't want
# the savegame stuff to depend on the data library.)
#
# We're including Resurrect Travel and Location Travel stations as well,
# in case those pop up too.

data = BL3Data()

output_file = 'fts_mappings.py'

# Grab a list of object names
object_names = []
for base_path in [
        '/Game/GameData/FastTravel',
        '/Game/PatchDLC/BloodyHarvest/GameData/FastTravel',
        '/Game/PatchDLC/Raid1/GameData/FastTravel',
        '/Game/PatchDLC/Dandelion/GameData/FastTravel',
        '/Game/PatchDLC/Hibiscus/GameData/FastTravel',
        '/Game/PatchDLC/Event2/GameData/FastTravel',
        ]:
    for prefix in ['FTS_', 'RTS_', 'LTS_']:
        object_names.extend(list(data.find(base_path, prefix)))

# Construct the mapping
fts_mapping = {}
for object_name in object_names:
    object_name_full = Mod.get_full_cond(object_name).lower()
    obj = data.get_data(object_name)
    for exp in obj:
        if 'StationMapName' in exp:
            last_map_bit = exp['StationMapName'].split('/')[-1]
            fts_mapping[object_name_full] = last_map_bit
            break

# Now output as a Python dict
with open(output_file, 'w') as df:
    print('', file=df)
    print('# Autogenerated by gen_fts_mappings.py, in my bl3hotfixmodding project (in dataprocessing)', file=df)
    print('', file=df)
    print('fts_to_map = {', file=df)
    for k, v in sorted(fts_mapping.items()):
        print("        '{}': '{}',".format(k, v), file=df)
    print('        }', file=df)
    print('', file=df)

print('Generated {}'.format(output_file))
