from bl3hotfixmod import Mod 

mod=Mod('wotan_loot_test.txt',
'Wotan Loot Test',
'SSpyR',
[
    'Mod to up Wotans Drop Rate to test things.'
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Adjusting rate to 100%')
mod.table_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/Table_Legendary_SpecificLootOdds_Raid1',
'RaidBoss',
'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
1.00
)
mod.newline()

mod.comment('Adjusting quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
'Quantity',
'(BaseValueConstant=20)')
mod.newline()

mod.close()