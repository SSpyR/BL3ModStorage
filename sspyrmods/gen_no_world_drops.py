from bl3hotfixmod import Mod

# Make Legendaries not World Drop, Base Game First as a Test (It Works)
# For Base Game Firestorm (Nade) is the only thing that is World Drop only, add it back to Traunt
# Up Purple Drops to Compensate Maybe

mod=Mod('no_world_drops.txt',
'Legendaries No World Drop',
'SSpyR',
[
    'Taking Away World Drop Legendaries.',
    'Except Those That are Only World Drops'
],
lic=Mod.CC_BY_SA_40
)

pools=[
    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All',
    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All',
    '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts',
    '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_SniperAndHeavy_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_ARandSMG_All'
]

for pool in pools:
    mod.comment('Adjusting to Remove Legendaries')
    mod.reg_hotfix(Mod.PATCH, '',
    pool,
    'BalancedItems.BalancedItems[4].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()

mod.comment('Adding Firestorm Back to Traunt')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Heavy_Traunt',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_CaptTraunt',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)