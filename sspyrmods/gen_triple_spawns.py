from bl3hotfixmod import Mod
from bl3data import BL3Data
import os

# Utils: spawnoptions.txt
# Some enemy spawns may not be under and /Enemies directory (see Dandelion's CrewChallenges/Kill/ directory)
# Need SpawnerStyle Data to actual Triple Spawn stuff

mod=Mod('triple_spawns.bl3hotfix',
'Triple Spawns',
'SSpyR',
[
   'Mod that triples all enemy spawns.',
   'Except it doesnt actually :)',
   'Currently a Spawn Test ModFile'
],
lic=Mod.CC_BY_SA_40,
cats='spawns'
)

OakSpawners=[
    15,
    16,
    6,
    12,
    4,
    5
]

for spawn in OakSpawners:
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Desertvault_P',
    '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'NumActorsParam.AttributeInitializationData.BaseValueConstant',
    '10'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Desertvault_P',
    '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
    '10'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Desertvault_P',
    '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
    '10'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'Desertvault_P',
    '/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'NumAliveActorsParam.AttributeInitializationData.BaseValueConstant',
    '10'
    )
    mod.newline()
    #mod.reg_hotfix(Mod.EARLYLEVEL, 'Desertvault_P',
    #'/Game/Maps/Zone_3/DesertVault/Desertvault_Dynamic.Desertvault_Dynamic:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    #'SpawnOptions',
    #Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
    #)
    #mod.newline()

OakSpawners2=[
   71,
   88,
   89,
   90,
   91
]

for spawn2 in OakSpawners2:
    mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
    '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'NumActorsParam.AttributeInitializationData.BaseValueConstant',
    '60'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
    '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'MaxAliveActorsWhenPassive.AttributeInitializationData.BaseValueConstant',
    '60'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
    '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'MaxAliveActorsWhenThreatened.AttributeInitializationData.BaseValueConstant',
    '60'
    )
    mod.newline()
    mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
    '/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat:PersistentLevel.OakMissionSpawner_{}.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den'.format(spawn),
    'SpawnOptions',
    Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
    )
    mod.newline()
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat.PersistentLevel.OakMissionSpawner.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
'SpawnOptions',
Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
)
mod.newline()
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat.PersistentLevel.Spawner_SpawnAnchorEridian.SpawnerComponent.SpawnerStyle_Encounter.SpawnerStyle_SpawnerStyle_Den',
'SpawnOptions',
Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
)
mod.newline()
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat.PersistentLevel.OakMissionSpawner.SpawnerComponent.SpawnerStyle_SpawnerStyle_Den',
'SpawnOptions',
Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
)
mod.newline()
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat.PersistentLevel.OakMissionSpawner.SpawnerComponent.SpawnerStyle_Den',
'SpawnOptions',
Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
)
mod.newline()
mod.reg_hotfix(Mod.EARLYLEVEL, 'GuardianTakedown_P',
'/Game/PatchDLC/Takedown2/Maps/GuardianTakedown_Combat.GuardianTakedown_Combat.PersistentLevel.OakMissionSpawner.SpawnerComponent.SpawnerStyle_SpawnerStyle_Encounter.SpawnerStyle_Den',
'SpawnOptions',
Mod.get_full_cond('/Game/Enemies/_Spawning/Ape/_Mixes/SpawnOptions_ApeMix', 'SpawnOptionData')
)
mod.newline()

#data=BL3Data()

#dir=os.path.dirname(__file__)

#spawnoptions=open(os.path.join(dir, 'spawnoptions.txt')).readlines()

#for spwop in spawnoptions:
#    allexports=data.get_data(spwop)
#    try:
#        optdata=data.get_exports(spwop, 'SpawnOptionData')[0]
#        for idx, option in enumerate(optdata['Options']):
#            alivelimit=option['AliveLimit']
#            print(alivelimit)
#            alivelimit=alivelimit*3

#            mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
#            str.rstrip(spwop),
#            'Options.Options[{}].AliveLimit'.format(idx),
#            alivelimit
#            )
#            mod.newline()

#            alivelimitparam=option['AliveLimitParam']['Range']['Value']
#            print(alivelimitparam)
#            alivelimitparam=alivelimitparam*3

#            mod.reg_hotfix(Mod.EARLYLEVEL, 'MatchAll',
#            str.rstrip(spwop),
#            'Options.Options[{}].AliveLimitParam.Range'.format(idx),
#            '(Value={})'.format(alivelimitparam)
#            )
#            mod.newline()

#    except IndexError:
#        print('No Exports of Type SpawnOptionData')

mod.close()