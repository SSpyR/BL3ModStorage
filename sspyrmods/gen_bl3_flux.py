from bl3hotfixmod import Mod, Balance

# I think its time for the big big mod

# No World Drop Legendaries (Done for Base Game)
# Adjust Some Drop Rates and Pools
# COMs Roll More Sub-Stats
# Adjust Mayhem Scaling on Stuff (Done, can maybe do more)
# Nerf Stinger Base (Maybe Done?)
# Grenade Buffs
# Nerf Ties
# Buff Non-Uniques


mod=Mod('bl3_flux.txt',
'BL3 Flux Mod',
'SSpyR',
[
    'My personal take on a large-scale overhaul mod for Borderlands 3.',
    'This mod takes things from some of my other mods and puts them together with a',
    'bunch of other changes, examples being: No More Anoints, Melee Can Crit, Skill Formula Adjustments',
    'and more. This mod so far is very much in the early stages and some portions could likely be made',
    'irrelevant by Gearbox at some point but it will be an active project for right now.'
],
lic=Mod.CC_BY_SA_40,
)

# No World Drop Legendaries (Only Base Game rn, do DLCs soon)
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
    mod.comment('Adjusting to Remove Legendaries from World Drops')
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
mod.newline()


# No Anoints 
anoints=[
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_AccuracyHandling/GPart_All_SkillEnd_AccuracyHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CooldownRate/GPart_All_SkillEnd_CooldownRate',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_CritDamage/GPart_All_SkillEnd_CritDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_DamageReduction/GPart_All_SkillEnd_DamageReduction',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_EleChanceDamage/GPart_All_SkillEnd_EleChanceDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_FireRateReload/GPart_All_SkillEnd_FireRateReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_HealthRegen/GPart_All_SkillEnd_HealthRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_LifeSteal/GPart_All_SkillEnd_LifeSteal',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MeleeDamage/GPart_All_SkillEnd_MeleeDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_MoveSpeed/GPart_All_SkillEnd_MoveSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Corrosive/GPart_All_SkillEnd_NextMagBonusDamageCorrosive',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Cryo/GPart_All_SkillEnd_NextMagBonusDamageCryo',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Fire/GPart_All_SkillEnd_NextMagBonusDamageFire',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Radiation/GPart_All_SkillEnd_NextMagBonusDamageRadiation',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_NextMagBonus/Shock/GPart_All_SkillEnd_NextMagBonusDamageShock',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_ProjectileSpeed/GPart_All_SkillEnd_ProjectileSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_SplashDamage/GPart_All_SkillEnd_SplashDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_UniqueEnemyDamage/GPart_All_SkillEnd_UniqueEnemyDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillEnd_WeaponDamage/GPart_All_SkillEnd_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/_Generic/SkillStart_AddGrenade/GPart_All_SkillEnd_AddGrenade',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandLifeSteal/GPart_Beast_AttackCmd_Lifesteal',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/AttackCommandMovespeed/GPart_Beast_AttackCmd_Movespeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/Beast_Gamma_BonusRadiationDamage/GPart_BonusRadiationDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkAttackCharge/GPart_Beast_RakkCharge',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkSlag/GPart_Beast_RakkSlag',
    'Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/RakkUsed_CritDamage/GPart_Beast_RakkCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthAccuracyHandling/GPart_Beast_Stealth_AccuracyHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Beastmaster/StealthNova/GPart_Beast_ExitStealthNova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_AmmoRegen/GPart_Gunner_AutoBear_AmmoRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/AutoBear_FireDamage/GPart_Gunner_AutoBear_FireDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/EnterExit_Nova/GPart_Gunner_EnterExit_Nova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_KillsLowerCooldown/GPart_Gunner_KillsLowerCooldown',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFireDamage/GPart_Gunner_NextMagFireDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagFirerateCrit/GPart_Gunner_NextMagFirerateCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NextMagReloadHandling/GPart_Gunner_NextMagReloadHandling',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_NoAmmoConsumption/GPart_Gunner_NoAmmoConsumption',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_ShieldMaxHealth/GPart_Gunner_ShieldHealthMax',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/Exit_SplashDamageIncrease/GPart_Gunner_SplashDamageIncrease',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Gunner/IBActive_ChanceGrenade/GPart_Gunner_IBGrenadeChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActive_StatusEffectChance/GPart_Operative_BarrierActive_StatusEffectChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierActiveAccuracyCrit/GPart_Operative_BarrierActive_AccuracyCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/BarrierDeployShieldRecharge/GPart_Operative_BarrierDeploy_ShieldRecharge',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveHealthRegen/GPart_Operative_CloneActive_HealthRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneActiveRegenAmmo/GPart_Operative_CloneActive_AmmoRegen',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapDamage/GPart_CloneSwap_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/CloneSwapInstaReload/GPart_Operative_CloneSwapInstaReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveBonusDamage/GPart_Operative_DroneActiveBonusDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveFireRateReload/GPart_Operative_DroneActive_FireRateReload',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Operative/DroneActiveMovespeed/GPart_Operative_DroneActiveMovespeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_EleChance/GPart_Siren_Cast_ElementalChance',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Cast_WeaponDamage/GPart_Siren_Cast_WeaponDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_AccuracyCrit/GPart_Siren_Grasp_AccuracyCrit',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ChargeSpeed/GPart_Siren_Grasp_ChargeSpeed',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Grasp_ConstantNova/GPart_Siren_Grasp_ConstantNova',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/SkillEnd_AttunedEleDamage/GPart_Siren_SkillEnd_AttunedSkillDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_DamageReduction/GPart_Siren_Slam_DamageReduction',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_MeleeDamage/GPart_Siren_Slam_MeleeDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_ReturnDamage/GPart_Siren_Slam_ReturnDamage',
    '/Game/Gear/Weapons/_Shared/_Design/EndGameParts/Character/Siren/Slam_WeaponDamage/GPart_Siren_Slam_WeaponDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ConsecutiveHits_DmgStack/GPart_EG_Generic_ConsecutiveHitsDmgStack',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/GrenadeThrow_GlobalDamage/GPart_EG_GrenadeThrow_GlobalDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/KillStack_ReloadDamage/GPart_EG_Generic_KillStackReloadDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/LowHealth_Executor/GPart_EG_Generic_LowHealthExecutor',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/ModeSwitch_WeaponDamage/GPart_EG_ModeSwitch_WeaponDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Corrosive/GPart_EG_SkillEndBonusEleDamage_Corrosive',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Cryo/GPart_EG_SkillEndBonusEleDamage_Cryo',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Fire/GPart_EG_SkillEndBonusEleDamage_Fire',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Radiation/GPart_EG_SkillEndBonusEleDamage_Radiation',
    '/Game/PatchDLC/Raid1/Gear/Anointed/Generic/SkillEnd_BonusEleDamage_Shock/GPart_EG_SkillEndBonusEleDamage_Shock',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/AccuracyAndHandling/GPart_EG_WhileAirborn_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/CritDamage/GPart_EG_WhileAirborn_CritDamage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/Damage/GPart_EG_WhileAirborn_Damage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileAirborn/FireRate/GPart_EG_WhileAirborn_FireRate',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/AccuracyAndHandling/GPart_EG_WhileSliding_AccuracyHandling',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/Damage/GPart_EG_WhileSliding_Damage',
    '/Game/PatchDLC/Raid1/Gear/Anointed/WhileSliding/FireRate/GPart_EG_WhileSliding_FireRate',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_All_CritStatusEffects/GPart_Passive_All_CritStatusEffect',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_All_RadDamage/GPart_All_unhealthyraddamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_HighHealth_Breaker/GPart_All_HighHealthBreaker',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_ShieldBreakAmp/GPart_All_ShieldBreakAmp',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/Passive_SlideRegenShields/GPart_All_SlideRegenShields',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_CyberSpike/GPart_EG_Gen_SkillEnd_CyberSpike',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_DamageMitigation/GPart_All_DamageMitigation',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_GrenadeDamage/GPart_All_GrenadeDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_PulseNova/GPart_EG_Gen_SkillActive_PulseFireNova',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_ShockFeedback/GPart_All_ShockFeedback',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_UniqueEnemyDamage/GPart_All_UniqueEnemyDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillActive_WeaponDamage/GPart_All_WeaponDamage',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillEnd_HealingPool/GPart_All_HealingPool',
    '/Game/PatchDLC/Event2/Gear/Weapon/EndGameParts/_Generic/SkillStart_ShieldRecharge/GPart_All_SkillStart_OverchargeShield'
]

for anoint in anoints:
    mod.comment('Removing from Pool')
    mod.reg_hotfix(Mod.PATCH, '',
    anoint,
    'MinGameStage',
    '(BaseValueConstant=100.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)'
    )
    mod.newline()


# Mayhem 2 No Modifiers
mod.comment('Setting Easy Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_EAsy.ModSet_Mayhem2_EAsy',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/PartyTime/Ability_Mayhem2_PartyTime.Ability_Mayhem2_PartyTime_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/AimForTheSky/Ability_Mayhem2_AimForTheSky.Ability_Mayhem2_AimForTheSky_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RoidRage/Ability_Mayhem2_RoidRage.Ability_Mayhem2_RoidRage_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/SoulStealer/Ability_Mayhem2_SoulStealer.Ability_Mayhem2_SoulStealer_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Shared/Bighetti/Ability_Mayhem2_Bighetti.Ability_Mayhem2_Bighetti_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FinishThem/Ability_Mayhem2_FinishThem.Ability_Mayhem2_FinishThem_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Medium Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Medium.ModSet_Mayhem2_Medium',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/FloorIsLava/Ability_Mayhem2_FLoorIsLava.Ability_Mayhem2_FloorIsLava_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/FrozenPulse/Ability_Mayhem2_FrozenPulse.Ability_Mayhem2_FrozenPulse_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/Rally/Ability_Mayhem2_Rally.Ability_Mayhem2_Rally_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/OlSwitcheroo/Ability_Mayhem2_OlSwitcheroo.Ability_Mayhem2_OlSwitcheroo_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Corrosive.Ability_Mayhem2_ElementalInfusion_Corrosive_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Cryo.Ability_Mayhem2_ElementalInfusion_Cryo_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Fire.Ability_Mayhem2_ElementalInfusion_Fire_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Radiation.Ability_Mayhem2_ElementalInfusion_Radiation_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_Shock.Ability_Mayhem2_ElementalInfusion_Shock_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/HealNo/Ability_Mayhem2_HealNo.Ability_Mayhem2_HealNo_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Hard Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_Hard.ModSet_Mayhem2_Hard',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ChainGang/Ability_Mayhem2_ChainGang.Ability_Mayhem2_ChainGang_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ArcaneEnchanter/Ability_Mayhem2_ArcaneEnchanter.Ability_Mayhem2_ArcaneEnchanter_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DroneBuddy/Ability_Mayhem2_DroneBuddy.Ability_Mayhem2_DroneBuddy_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/EleBreaker/Ability_Mayhem2_Ele_Breaker.Ability_Mayhem2_Ele_Breaker_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/StayBack/Ability_Mayhem2_StayBack.Ability_Mayhem2_StayBack_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/BegoneDot/Ability_Mayhem2_BegoneDot.Ability_Mayhem2_BegoneDot_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()

mod.comment('Setting Very Hard Modifiers Weights to 0')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard.ModSet_Mayhem2_VeryHard',
'ModifierSets',
"""
(
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/DeathFromBeyond/Ability_Mayhem2_DeathFromBeyond.Ability_Mayhem2_DeathFromBeyond_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/RogueLite/Ability_Mayhem2_RogueLite.Ability_Mayhem2_RogueLite_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/CriticalFailure/Ability_Mayhem2_CritFail.Ability_Mayhem2_CritFail_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Player/Sharpshot/Ability_Mayhem2_Sharpshot.Ability_Mayhem2_Sharpshot_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/PriorityTarget/Ability_Mayhem2_PriorityTarget.Ability_Mayhem2_PriorityTarget_C,
        Weight=(BaseValueConstant=0)
    ),
    (
        ModifierAbility=/Game/PatchDLC/Mayhem2/Abilities/Enemy/ElementalInfusion/Ability_Mayhem2_ElementalInfusion_All.Ability_Mayhem2_ElementalInfusion_All_C,
        Weight=(BaseValueConstant=0)
    )
)
""")
mod.newline()


# Mayhem Scaling Balancing
# /Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet (1-10) <- Modifier Table
enemyhp=[
"HealthSimpleScalar_42_0499AACF43FDF39B7084E2BB63E4BF68",
"ArmorSimpleScalar_44_BCAAA445479831C25B0D55AF294A15D6",
"ShieldSimpleScalar_43_417C36C54DA2550A4CABC7B26A5E24A8"
]
exp="ExpGainScalar_39_2159F009466933AA733AE688E55B1B93"
cash="CashScalar_22_B7B11DC94BBB45C94A96279146EC193E"
drop1="DropWeightCommonScalar_21_59A2FB124E32B955768A7B9D93C25A99"
drop2="DropWeightUncommonScalar_25_809615334E7F0DB3B8712DAC221015C3"
drop3="DropWeightRareScalar_27_A09CF5314C51796896A83EA0806C7520"
drop4="DropWeightVeryRareScalar_29_F2CA570046CD50A7C514EDB0AE1BE591"
drop5="DropWeightLegendaryScalar_31_D9DA03C54065EA981BE218B11942C24E"
dropnum="DropNumberChanceSimpleScalar_40_115637764B3918F01E6FAFADDC005388"
eridium="DropEridiumChanceSimpleScalar_41_E89AD7E9473FDF3CBED395BA6641FA68"
loot="LootQuality_56_03E220E0495C6B37CD6C7195F5EA289B"
asd="DamageScalarActionSkill_60_39AF483140740A38FC71BA897155CBFF"
melee="DamageScalarMelee_67_9948929F4FF34364CED2EAB51A881946"
slide="DamageScalarSlide_68_B48D0E3A4DF57196839BB58D5AE3E638"
slam="DamageScalarSlam_69_15DB6EDC4CCA52620BF25398CFFD9B26"
petdmg="DamageScalarPet_72_0DD7977D44C4A71D0A6B56B7884E023C"
env="DamageScalarEnviornmental_111_E2A582AA47FC000789FC68BBD31D2CFC"
passiveskill="DamageScalarPassive_115_6A30229E4CC04F751ED01CB64A71880F"
vehicledmg="DamageDealtScalarVehicles_103_5739171948322B35CDA36487F78AF0CE"
vehiclehp="DamageTakenScalarVehicles_104_B75AB4EC482624FDEAAF31B0FA369A77"
gear="DamageScalarGear_119_9FC89117424C6619F2CA958FA2842FC2"
pethp="PetHealth_84_E5B903B4452F4310CCD13C931474E12B"
comphp="CompanionHealth_89_294A6BE7439072AE9F934CAA127D8D83"

# Enemy HP Adjustments (Cutting by 50% for Right Now)
for hptype in enemyhp:
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '1',
    hptype,
    1.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '2',
    hptype,
    2.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '3',
    hptype,
    3.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '4',
    hptype,
    4.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '5',
    hptype,
    7.5
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '6',
    hptype,
    15.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '7',
    hptype,
    22.50
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '8',
    hptype,
    30.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '9',
    hptype,
    40.0
    )
    mod.newline()
    mod.comment('Adjusting HP Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    '10',
    hptype,
    50.0
    )
    mod.newline()

# Melee Buff (Doubling for Now)
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
melee,
2.4
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
melee,
2.8
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
melee,
3.2
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
melee,
3.6
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
melee,
5.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
melee,
8.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
melee,
11.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
melee,
14.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
melee,
18.0
)
mod.newline()
mod.comment('Adjusting Melee Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
melee,
32.0
)
mod.newline()

# AS Damage Buffing (Doubling for Now)
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
asd,
3.2
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
asd,
4.4
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
asd,
5.6
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
asd,
6.8
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
asd,
11.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
asd,
20.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
asd,
29.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
asd,
38.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
asd,
50.0
)
mod.newline()
mod.comment('Adjusting AS Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
asd,
61.0
)
mod.newline()

# Pet Damage Buffing (Doubling for Now)
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'1',
asd,
4.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'2',
asd,
6.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'3',
asd,
8.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'4',
asd,
10.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'5',
asd,
17.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'6',
asd,
32.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'7',
asd,
47.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'8',
asd,
62.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'9',
asd,
82.0
)
mod.newline()
mod.comment('Adjusting Pet Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
'10',
asd,
102.0
)
mod.newline()

# Getting Rid of Mayhem Scaling on Skills
mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Passive Skill Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    passiveskill,
    0
    )
    mod.newline()
    mlevel+=1


# Melee Crit
mod.comment('Making Melee Crit (10 FPSs Credit Here)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/DamageSources/DamageSource_Melee.Default__DamageSource_Melee_C',
'bCanCauseCriticals',
'true'
)
mod.newline()


# Stinger Nerf
mod.comment('Removing Nova Berner Scaling')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[0]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[1]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Parts/Part_Shield_Aug_Stinger',
'SecondaryStackValues.SecondaryStackValues[2]',
'DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\")'
)
mod.newline()


# Formula Balancing (Basically Just Giving V1 to People Except FL4K)
# V1 Damage Below
# "AttributeData": [
# "Att_DamageDealtMultiplier",
# "/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier"
# Tenacious Defense, Click Click, Desperate Measures, Samsara, Jab Cross, Donnybrook, Confident Competence 
# Seems Only Status File is Needed for Actual Values, Passive is Needed for UI
# Buff Samsara and Wrath Here too
# Probably Buff FL4K in Some Areas

passive_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/PassiveSkill_Gunner_LowHPDamage.PassiveSkill_Gunner_LowHPDamage_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Passive_Gunner_Tenacious.Passive_Gunner_Tenacious_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/PassiveSkill_Gunner_ClickClick.PassiveSkill_Gunner_ClickClick_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/Donnybrook/PassiveSkill_Operative_Donnybrook.PassiveSkill_Operative_Donnybrook_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/PassiveSkill_Operative_ConfidentCompetence.PassiveSkill_Operative_ConfidentCompetence_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/PassiveSkill_Siren_Samsara.PassiveSkill_Siren_Samsara_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/PassiveSkill_Siren_BareKnuckle.PassiveSkill_Siren_BareKnuckle_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute'
]
status_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/Status_FullCan_LowHPDamage_P',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Status_Gunner_Tenacious_WeaponDamage_DA',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/StatusEffect_Gunner_ClickClick_WeaponDamage_DA',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/Donnybrook/StatusEffect_Operative_Donnybrook',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/StatusEffect_Operative_ConfidentCompetence',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/StatusEffect_Siren_Samsara',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/StatusEffect_Siren_BareKnuckle_DA'
]

mod.comment('Making Skills V1')
for status in status_to_v1:
    mod.reg_hotfix(Mod.PATCH, '',
    status,
    'AttributeEffects.AttributeEffects[0].AttributeData',
    '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
    )
    mod.newline()

# UI Change Still Not Working, Will Look Into
mod.comment('Adjusting Cards for V1 Changes')
for passive in passive_to_v1:
    mod.reg_hotfix(Mod.PATCH, '',
    passive,
    'Attribute',
    '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
    )
    mod.newline()


# Adding 2 More SubStats to COMs (Doesn't Seem to Work Currently, Look Further Into It)
mod.comment('Increasing SubStat Rolls')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/ClassMods/_Design/PartSets/PartSet_ClassMod',
'ActorPartLists.ActorPartLists[3].MultiplePartSelectionRange',
'(Min=3,Max=3)'
)
mod.newline()