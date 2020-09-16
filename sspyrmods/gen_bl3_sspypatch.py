from bl3hotfixmod import Mod, Balance, ItemPool, ItemPoolEntry, BVC
from bl3data import BL3Data

# Adjust sell price of customizations
# Purple E-Tech Pistols
# Adjust self-splash damage if possible
# Give Mission Only Rewards to something (Ember's Purge to Stanley Bot, Scoville to Tony Bordel)
# Grenades from Loaders in DLC1 bypass Player Shields?
# Vibra Pulse and Moxxi's Embrace to pool with Crit and Hail
# Maybe give some specific mod packs specific drops (like Cobra in BL2)
# Add in Scrapped Legendaries that are completely (Heckle and Hyde, Networker, RYNAH, etc.)
# Leave World Drop Artifacts and Class Mods until I can adjust their RNG

"""
FiringPatternLines(0)=
(
    StartPoint =
    (Pitch=4369,Yaw=0,Roll=0),
    EndPoint =
    (Pitch=0,Yaw=0,Roll=0),
    bUseStartPointOnly = True,
    CustomWaveMotion =
    (
        bUseCustomWaveMotion = False,
        WaveFreq =
        (X=0.000000,Y=0.000000,Z=0.000000),
        WaveAmp =
        (X=0.000000,Y=0.000000,Z=0.000000),
        WavePhase =
        (X=0.000000,Y=0.000000,Z=0.000000)
    )
)
"""

# Balance Idea List
"""
Destructor Spinner Buff
Rebel Yell Buff
Either Give Zane V1 to something other than Donnybrook, or nerf DB numbers (likely the latter)
Adjust Hail's firing arc to more akin to BL2's (see BL2's for reference)
Change some Legendaries to Blues and Purps (M6 and M4 Legendaries are good idea for this +_others)
Maybe make only utility anoints thing?
Barrels are still fucking Barrels
Look into probably nerfing Facepuncher
"""

mod=Mod('bl3_sspypatch.txt',
'BL3 SspyPatch',
'SSpyR',
[
    'My personal take on a large-scale overhaul mod for Borderlands 3.',
    'This mod takes things from some of my other mods and puts them together with a',
    'bunch of other changes, examples being: No More Anoints, Melee Can Crit, Skill Formula Adjustments',
    'and more. This mod so far is very much in the early stages and some portions could likely be made',
    'irrelevant by Gearbox at some point but it will be an active project for right now.',
    'Name Credit: Pirek'
],
lic=Mod.CC_BY_SA_40,
)

###
### LOOT ADJUSTMENTS
###

# No World Drop Legendaries 
pools=[
    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_All',
    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_All',
    '/Game/Gear/Artifacts/_Design/ItemPools/ItemPool_Artifacts',
    '/Game/Gear/ClassMods/_Design/ItemPools/ItemPool_ClassMods',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_Pistols_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_SniperAndHeavy_All',
    '/Game/GameData/Loot/ItemPools/Guns/ItemPool_ARandSMG_All',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Shields_All_Hibiscus',
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_GrenadeMods_All_Geranium'
]

for pool in pools:
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    pool,
    'BalancedItems.BalancedItems[4].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()

dlcpools=[
    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion',
    '/Game/PatchDLC/Dandelion/GameData/Loot/ItemPool_Guns_All_Dandelion_Boss',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_Guns_All_Hibiscus',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/ItemPool_GrenadeMods_All_Hibiscus', 
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Guns_All_Geranium',
    '/Game/PatchDLC/Geranium/GameData/Loot/ItemPool_Shields_All_Geranium',
    '/Game/PatchDLC/Alisma/GameData/Loot/ItemPool_Guns_All_Alisma',
    '/Game/PatchDLC/Alisma/GameData/Loot/ItemPool_Shields_All_Alisma'
]

for dlcpool in dlcpools:
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    dlcpool,
    'BalancedItems.BalancedItems[4].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    dlcpool,
    'BalancedItems.BalancedItems[5].Weight',
    '(BaseValueConstant=0,BaseValueAttribute=None,BaseValueScale=0)'
    )
    mod.newline()

legendary=[
    '/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Legendary',
    '/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Legendary',
    '/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SnipeRifles_Legendary',
    '/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Legendary',
    '/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Legendary',
    '/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Legendary',
    '/Game/GameData/Loot/ItemPools/Shields/ItemPool_Shields_05_Legendary',
    '/Game/GameData/Loot/ItemPools/GrenadeMods/ItemPool_GrenadeMods_05_Legendary',
    '/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Guns_Legendary',
    '/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Shields_Legendary',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary',
    '/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Shields_Legendary',
    '/Game/PatchDLC/Geranium/GameData/Loot/Legendary/ItemPool_Geranium_Guns_Legendary',
    '/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Guns_Legendary',
    '/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Shields_Legendary'
]

for wdrop in legendary:
    mod.comment('Adjusting to Remove Legendaries from World Drops')
    mod.reg_hotfix(Mod.PATCH, '',
    wdrop,
    'BalancedItems',
    """
    (
    )
    """
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

mod.comment('Giving Wendigo Seeryul Killur')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Wendigo',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SparkyBoom',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Wendigos Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Wendigo',
'/Hibiscus/Enemies/Wendigo/Design/Character/BPChar_Wendigo.BPChar_Wendigo_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[1].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Amach Old God')
mod.reg_hotfix(Mod.CHAR, 'BPChar_ZealotPilfer_Child_Rare',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Amachs Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_ZealotPilfer_Child_Rare',
'/Hibiscus/Enemies/_Unique/Rare_ZealotPilfer/Character/BPChar_ZealotPilfer_Child_Rare.BPChar_ZealotPilfer_Child_Rare_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Gmork Insider')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Gmork_B_Wolf_Child',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Gmorks Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Gmork_B_Wolf_Child',
'/Hibiscus/Enemies/_Unique/Hunt_Gmork/Character/BPChar_Gmork_B_Wolf_Child.BPChar_Gmork_B_Wolf_Child_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Empowered Grawn Torch')
mod.reg_hotfix(Mod.CHAR, 'BPChar_LunaticPossessed',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Lunacy',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy.InvBalD_Artifact_Lunacy,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy.InvBalD_Artifact_Lunacy\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Empowered Grawns Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_LunaticPossessed',
'/Hibiscus/Enemies/Lunatic/Possessed/_Design/Character/BPChar_LunaticPossessed.BPChar_LunaticPossessed_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=30.00)'
)
mod.newline()

mod.comment('Giving Kritchy Oldridian')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Hib_Hunt_Kritchy',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Mothman',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Kritchys Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Hib_Hunt_Kritchy',
'/Hibiscus/Enemies/_Unique/Hunt_Kritchy/Character/BPChar_Hib_Hunt_Kritchy.BPChar_Hib_Hunt_Kritchy_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=50.00)'
)
mod.newline()

mod.comment('Giving Fungal Gorger Flama Diddle')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Lost_Mush_Child',
'/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Mutant',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Upping Fungal Gorgers Dedicated Pool Rate to Compensate')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Lost_Mush_Child',
'//Hibiscus/Enemies/_Unique/Rare_MushroomGiant/Character/BPChar_Lost_Mush_Child.BPChar_Lost_Mush_Child_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools.ItemPools[0].PoolProbability',
'(BaseValueConstant=70.00)'
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
    mod.comment('Removing Anoint from Pool')
    mod.reg_hotfix(Mod.PATCH, '',
    anoint,
    'MinGameStage',
    '(BaseValueConstant=100.000000,DataTableValue=(DataTable=None,RowName=\"\",ValueName=\"\"),BaseValueAttribute=None,AttributeInitializer=None,BaseValueScale=1.000000)'
    )
    mod.newline()


# Adding Trials Dedicated Pools to the Guardian Gem Goblin
mod.comment('Adding the Pools to Gem Goblin')
mod.reg_hotfix(Mod.CHAR, 'BPChar_GuardianGemGoblin',
'/Game/Enemies/Guardian/_Unique/GemGoblin/_Design/Character/BPChar_GuardianGemGoblin.BPChar_GuardianGemGoblin_C:AIBalanceState_GEN_VARIABLE',
'DropOnDeathItemPools.ItemPools',
"""
(
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSkag.ItemPool_TrialBossSkag\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGuardian.ItemPool_TrialBossGuardian\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossTink.ItemPool_TrialBossTink\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossGoon.ItemPool_TrialBossGoon\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossMech.ItemPool_TrialBossMech\"',
        PoolProbability=(BaseValueConstant=0.100000)
    ),
    (
        ItemPool=ItemPoolData'\"/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_TrialBossSaurian.ItemPool_TrialBossSaurian\"',
        PoolProbability=(BaseValueConstant=0.100000)
    )
)
""")
mod.newline()


# Adding DLC World Drop Legendaries to Gun Gun Alt Fire (This might have been made obsolete oops)
mod.comment('Adding DLC World Drops to Gun Gun')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns_AltFire',
'BalancedItems',
"""
(
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/Guns/ItemPool_Guns_Legendary.ItemPool_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
        Weight=(BaseValueConstant=0.25,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Dandelion/GameData/Loot/Legendary/ItemPool_Dandelion_Guns_Legendary.ItemPool_Dandelion_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hibiscus_Guns_Legendary.ItemPool_Hibiscus_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Geranium/GameData/Loot/Legendary/ItemPool_Geranium_Guns_Legendary.ItemPool_Geranium_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Alisma/GameData/Loot/Legendary/ItemPool_Alisma_Guns_Legendary.ItemPool_Alisma_Guns_Legendary\"',
        Weight=(BaseValueConstant=1,,BaseValueScale=1)
    )
)
"""
)
mod.newline()


# Make Veterans Machine Only Quest Rewards (Adjust this if I bring some Anoints back)
# getall ItemPoolData BalancedItems name=DA_ItemPool_VendingMachine_CrazyEarl
mod.comment('Adjusting Veterans Machine Pool')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl',
'BalancedItems',
"""
(
    (
        ItemPoolData=ItemPoolData'\"/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards.DA_ItemPool_VendingMachine_CrazyEarl_MissionRewards\"',
        Weight=(BaseValueConstant=3,DataTableValue=(),BaseValueAttribute=GbxAttributeData'\"/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare\"'BaseValueScale=0.3),
        Quantity=(BaseValueConstant=9)
    )
)
"""
)
mod.newline()


# Adding Heckle and Hyde as Drops
mod.comment('Adding in Heckle and Hyde')
mod.reg_hotfix(Mod.CHAR, 'BPChar_Goliath_Bounty01',
'/Game/GameData/Loot/ItemPools/Unique/ItemPool_Pestilence_HeckleandHyde.ItemPool_Pestilence_HeckleandHyde',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1) 
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)
mod.newline()

mod.comment('Adjust Drop Rate Accordingly')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Table_LegendarySpecificLootOdds.Table_LegendarySpecificLootOdds',
'HeckleAndHyde',
'LegendaryDropChance_Playthrough2_50_11E6C8E8493E0A73AF9B35891E7CE111',
0.60
)
mod.newline()


# Adjust Maliwan Takedown Loot Pools and Adding P2P Networker
mod.comment('Adjusting weights and pool (adding Networker too)')
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
        InventoryBalanceData=/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries\"',
        Weight=(BaseValueConstant=1,BaseValueScale=0.60)
    ),
    (
        ItemPoolData=ItemPoolData'\"/Game/PatchDLC/Raid1/Customizations/ItemPool_Raid1_Customization.ItemPool_Raid1_Customization\"',
        Weight=(BaseValueConstant=1)
    )
)
""")
mod.newline()

mod.comment('Adjusting weights and pool')
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
        Weight=(BaseValueConstant=1,BaseValueScale=0.60)
    )
)
""")
mod.newline()


# Giving Crew Challenge Items and Mission Rewards from DLCs a Drop Location (Legendaries, not Uniques)
#mod.comment('Giving Embers Purge a Drop Source')
#mod.reg_hotfix(Mod.CHAR, '',
#''
#)
#mod.newline()

#mod.comment('Giving Scoville a Drop Source')
#mod.reg_hotfix(Mod.CHAR, '',
#''
#)
#mod.newline()

#mod.comment('Giving Rico a Drop Source')
#mod.reg_hotfix(Mod.CHAR, '',
#''
#)
#mod.newline()

#mod.comment('Giving Seventh Sense a Drop Source')
#mod.reg_hotfix(Mod.CHAR, '',
#''
#)
#mod.newline()

#mod.comment('Giving Pearl a Drop Source')
#mod.reg_hotfix(Mod.CHAR, '',
#''
#)
#mod.newline()



###
### MAYHEM MOD ADJUSTMENTS
###

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

# Getting Rid of Mayhem Scaling on Skills and Environmental Damage
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

mlevel=1
while mlevel <= 10:
    mod.comment('Adjusting Environmental Damage Values')
    mod.table_hotfix(Mod.PATCH, '',
    '/Game/PatchDLC/Mayhem2/Abilities/CoreModifierSets/Table_Mayhem2CoreModifierSet',
    mlevel,
    env,
    0
    )
    mod.newline()
    mlevel+=1



###
### BALANCE ADJUSTMENTS
###

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
# Probably Buff FL4K in Some Areas

passive_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/PassiveSkill_Gunner_LowHPDamage.Default__PassiveSkill_Gunner_LowHPDamage_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Passive_Gunner_Tenacious.Default__Passive_Gunner_Tenacious_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/PassiveSkill_Gunner_ClickClick.Default__PassiveSkill_Gunner_ClickClick_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/PassiveSkill_Operative_Multitasker.Default__PassiveSkill_Operative_Multitasker_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/PassiveSkill_Operative_ConfidentCompetence.Default__PassiveSkill_Operative_ConfidentCompetence_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/Samsara/PassiveSkill_Siren_Samsara.Default__PassiveSkill_Siren_Samsara_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute',
    '/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/BareKnuckle/PassiveSkill_Siren_BareKnuckle.Default__PassiveSkill_Siren_BareKnuckle_C:StatDataItems_UIStatData_OakPassiveAbilityAttribute'
]
status_to_v1=[
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/LowHpDamage/Status_FullCan_LowHPDamage_P',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_UrsaCorps/TenaciousDefense/Status_Gunner_Tenacious_WeaponDamage_DA',
    '/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/ClickClick/StatusEffect_Gunner_ClickClick_WeaponDamage_DA',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/BarrierTree/ConfidentCompetence/StatusEffect_Operative_ConfidentCompetence',
    '/Game/PlayerCharacters/Operative/_Shared/_Design/Passives/CloneTree/MultiTasker/StatusEffect_Operative_Multitasker',
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

mod.comment('Adjusting Cards for V1 Changes')
for passive in passive_to_v1:
    mod.reg_hotfix(Mod.PATCH, '',
     passive,
    'Attribute',
    '/Game/GameData/Attributes/Damage/Att_DamageDealtMultiplier.Att_DamageDealtMultiplier'
    )
    mod.newline()

for passive in passive_to_v1:
    desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$'
    if 'LowHPDamage' in passive or 'ConfidentCompetence' in passive or 'ClickClick' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] Up to $VALUE$'
    if 'Samsara' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$ per enemy damaged'
    if 'Multitasker' in passive:
        desc='[skillbold]Bonus Damage:[/skillbold] $VALUE$ per active action skill'
    mod.reg_hotfix(Mod.PATCH, '',
    passive,
    'FormatText',
    desc
    )
    mod.newline()

mod.comment('Buffing Samsara Damage Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'Samsara_GunDamage',
'Value',
'(BaseValueConstant=0.0498)'
)
mod.newline()

mod.comment('Buffing Wrath Damage Values')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/Balance/Siren/DataTable_Siren_ConstantValues',
'Wrath_DamageBonus',
'Value',
'(BaseValueConstant=0.1665)'
)
mod.newline()


# Buffing Sniper Crit Bonus
mod.comment('Buffing Sniper Crit Bonus')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Base_Data.DataTable_Weapon_Base_Data',
'SniperRifle',
'CritDamageScale_61_5876F7BA4086CE2615C39F84E7409B3C',
1.5
)
mod.newline()


# Buffing Grenades Across the Board
mod.comment('Buffing Grenades')
mod.table_hotfix(Mod.PATCH, '',
'/Game/GameData/Balance/HealthAndDamage/DamageBalanceScalers/DataTable_Damage_GlobalBase.DataTable_Damage_GlobalBase',
'PlayerGrenadeModDamage',
'Base_2_5C32556442B4DA4D7EAE1A8610E0A950',
95
)
mod.newline()


# Buffing Uniques (Blue and Purple Rarity Weapons) Across the Board
mod.comment('Buffing Purples')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
'VeryRare',
'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
1.22
)
mod.newline()

mod.comment('Buffing Blues')
mod.table_hotfix(Mod.PATCH, '',
'/Game/Gear/Weapons/_Shared/_Design/GameplayAttributes/Weapon_Initialization/DataTable_Weapon_Rarity_Stats',
'Rare',
'DamageScale_6_44C1C8784B7991DCCCF68DA3127A53C0',
1.15
)
mod.newline()


# Changing Legendary Shield Amp
mod.comment('Adjusting Re-Router')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/Gear/Shields/_Design/_Uniques/Vamp/Parts/Part_Shield_Aug_ANS_LGD_ReRouter.Part_Shield_Aug_ANS_LGD_ReRouter:AspectList_ShieldAugmentAspectData.Augment_ShieldAug_VersionOmNom.ShotModifier_WeaponShotModifier',
'bDistributeBetweenProjectiles',
'false'
)
mod.newline()

mod.comment('Adjusting Version O.m')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Parts/Part_Shield_Aug_ANS_LGD_VersionOmNom.Part_Shield_Aug_ANS_LGD_VersionOmNom:AspectList_ShieldAugmentAspectData_0.Augment_ShieldAug_VersionOmNom.ShotModifier_WeaponShotModifier',
'bDistributeBetweenProjectiles',
'false'
)
mod.newline()



###
### MISC ADJUSTMENTS/FIXES
###

# Melee Crit
mod.comment('Making Melee Crit (10 FPSs Credit Here)')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/DamageSources/DamageSource_Melee.Default__DamageSource_Melee_C',
'bCanCauseCriticals',
'true'
)
mod.newline()


# Click Click Green Monster Fix
mod.comment('Fixing Green Monster Click Click Points')
gm_bal_name='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/InvBalD_CM_Gunner_DLC1'
clickclick_part='/Game/PatchDLC/Dandelion/Gear/CM/_D/PartSets/_U/GUN/Skills/ClassMod_Part_Skill_Gunner_ClickClikc_DLC1' 

data = BL3Data()
gm_bal = Balance.from_data(data, gm_bal_name)
for cat in gm_bal.categories:
    if cat.index == 5 & cat.num_max == 5:
        cat.add_part_name(clickclick_part, 1)
        cat.add_part_name(clickclick_part, 1)
        break
gm_bal.hotfix_full(mod)
mod.newline()


# Allowing FL4K Pets to Melee Crit
mod.comment('FL4K Pets Can Melee Crit')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/_Shared/_Design/DamageSources/DamageSource_BeastmasterPet_Melee.DamageSource_BeastmasterPet_Melee',
'bCanCauseCriticals',
'true'
)
mod.newline()


# Enabling Cartels Event (Credit to apocalyptech)
mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'LeagueInstance',
        1)
mod.newline()

mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/GameplayGlobals',
        'ActiveLeague',
        'OL_TheCartels')
mod.newline()

mod.comment('Global Cartel activation switches')
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/GameData/Spawning/GlobalSpawnDLCData',
        'DLCs',
        """(
            (
                Data=/Game/PatchDLC/Event2/GameData/SpawnDLCSCripts/SpawnDLC_Cartels.SpawnDLC_Cartels,
                IsEnabled=(BaseValueConstant=1.000000)
            )
        )""")
mod.newline()

mod.comment('Cartel Seasonal NPC')
mod.reg_hotfix(Mod.EARLYLEVEL, 'Sanctuary3_P',
        '/Game/Maps/Sanctuary3/Sanctuary3_Season.Sanctuary3_Season:PersistentLevel.OakMissionSpawner_1.SpawnerComponent.SpawnerStyle_SpawnerStyle_Single',
        'SpawnOptions',
        "SpawnOptionData'/Game/PatchDLC/Event2/NonPlayerCharacters/LeagueNPC/_Design/Spawning/SpawnOptions_LeagueNPC_Season02.SpawnOptions_LeagueNPC_Season02'")

mod.newline()

mod.comment('Cartel Main Menu')
mod.table_hotfix(Mod.PATCH, '',
        '/Game/Common/_Design/Table_MicropatchSwitches',
        'MainMenuAltBackground',
        'Value',
        BVC(bvc=5))
mod.newline()

mod.comment('Cartel Bugfixes')
mod.reg_hotfix(Mod.LEVEL, 'Cartels_P',
        '/Game/PatchDLC/Event2/Maps/Cartels_Mission.Cartels_Mission:PersistentLevel.OakMissionWaypointBox_ACtivateStairSlide.CollisionComp',
        'RelativeScale3D',
        '(X=1.000000,Y=1.000000,Z=1.600000)')
mod.newline()


# P2P Networker Secondary Element Fix (Credit to apocalyptech)
mod.comment('Fixing P2P Networker secondary element parts')
p2p_bal_name = '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link'
extra_elements = [
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_01_Fire',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_02_Cryo',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_03_Shock',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_04_Radiation',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/Parts/Elemental_Secondary/Part_SM_Mal_ElemSecondary_05_Corrosive',
        ]

data = BL3Data()
p2p_bal = Balance.from_data(data, p2p_bal_name)
for cat in p2p_bal.categories:
    if len(cat) == 0:
        cat.enabled = True
        for element in extra_elements:
            cat.add_part_name(element, 1)
        break
p2p_bal.hotfix_full(mod)
mod.newline()


# Fixing Purple E-Tech Pistols not Spawning
mod.comment('Fixing Purple E-Tech Pistols not Spawning')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_ETech_VeryRare',
'BalancedItems',
"""
(
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    ),
    (
        InventoryBalanceData=/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare,
        ResolvedInventoryBalanceData=InventoryBalanceData'\"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare\"',
        Weight=(BaseValueConstant=1,BaseValueScale=1)
    )
)
"""
)