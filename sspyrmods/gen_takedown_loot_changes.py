from bl3hotfixmod import Mod

mod=Mod('takedown_loot_changes.txt',
'Adjusting Takedown Loot Cause its Dumb',
[],
'TakedownLoot'
)

mod.comment('Adjusting weights and pools')
mod.reg_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Customizations/ItemPool_Raid1_Customization.ItemPool_Raid1_Customization\"',
        Weight=(BaseValueConstant=1)
    )
)
""")
mod.newline()

mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries\"',
        Weight=(BaseValueConstant=0,BaseValueScale=0)
    )
)
""")
mod.newline()

mod.comment('Adjusting quantity drops')
mod.reg_hotfix(Mod.CHAR, 'BPChar_BehemothRaid',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool',
'Quantity',
'(BaseValueConstant=2)')
mod.newline()

mod.reg_hotfix(Mod.CHAR, 'BPChar_MechRaidBossBar',
'/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool',
'Quantity',
'(BaseValueConstant=2)')
mod.newline()

mod.close()