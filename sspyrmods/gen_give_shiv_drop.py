from bl3hotfixmod import Mod 

mod=Mod('give_shiv_drop.txt',
'Example of Giving Shiv a Drop',
[],
''
)

mod.comment('Giving Shiv a Drop (HeadSplosion)')
mod.reg_hotfix(Mod.CHAR, 'BPChar_PsychoBadassPrologue',
'/Game/Enemies/Psycho_Male/_Unique/BadassPrologue/_Design/Character/BPChar_PsychoBadassPrologue.BPChar_PsychoBadassPrologue_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools',
"""
(
    (
        ItemPool=ItemPoolData'\"/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common.ItemPool_Shotguns_Common\"'
    ),
    (
        ItemPool=ItemPoolData'\"/Game/Missions/Plot/EP01_ChildrenOfTheVault/ItemPool_Prologue_Ammo.ItemPool_Prologue_Ammo\"',
        NumberOfTimesToSelectFromThisPool=(BaseValueConstant=3.000000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/Missions/Plot/EP01_ChildrenOfTheVault/ItemPool_Need_Prologue.ItemPool_Need_Prologue\"'
    ),
    (
        ItemPool=ItemPoolData'\"/Game/GameData/Loot/ItemPools/Unique/ItemPool_Headsplosion_Mothman.ItemPool_Headsplosion_Mothman\"',
        PoolProbability=(DataTableValue=(DataTable=DataTable'"/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds"',RowName="Shiv",ValueName="LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111")
    )
)
""")
mod.newline()

#mod.comment('Making 100% Drop Rate')
#mod.table_hotfix(Mod.CHAR, 'BPChar_PsychoBadassPrologue',
#'/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
#'Shiv',
#'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
#1.0)
#mod.newline()

mod.close()