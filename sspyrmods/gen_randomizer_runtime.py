from bl3hotfixmod import Mod, Balance
from bl3data import BL3Data

#Do Special Mags Too?

mod=Mod('randomizer_runtime.txt',
'Runtime Randomizer',
'SSpyR',
[
    'Runtime Randomizer for Borderlands 3 which randomizes',
    'parts within different pieces of gear (weapons, shields, grenades,',
    'class mods, and artifacts). Eventually I want to expand this to randomizing more',
    'things like enemy spawns (which should be possible?) and maybe skills if possible.'
    'This mod is unlike my manufacturer-specific randomizers where',
    'it randomizes all parts among all types and manufacturers which',
    'means that upon a save/quit things may break but it makes things a lot',
    'more crazy for sure. This is only the case for weapons however, other forms of gear',
    'stay upon a sasve/quit.'
],
lic=Mod.CC_BY_SA_40,
)

data=BL3Data()

#Weapons

#List the Balances
wbal_name=[
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_01_Common',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_02_Uncommon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_03_Rare',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse',
    '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun',
    '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki',
    '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_01_Common',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev',
    '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_01_Common',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_03_Rare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch',
    '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_01_Common',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_02_Uncommon',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_03_Rare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber',
    '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR',
    '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_02_UnCommon',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_03_rare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper',
    '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill',
    '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell',
    '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Balance/Balance_ATL_AR_Portals',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman',
    '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda',
    '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_01_Common',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_03_Rare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_01_Common',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_03_Rare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent',
    '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier',
    '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst',
    '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_01_Common',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_03_Rare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind',
    '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_01_Common',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius',
    '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_01_Common',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_03_Rare',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang',
    '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted',
    '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress',
    '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_01_Common',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_02_UnCommon',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter',
    '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_01_Common',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_03_Rare',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AureliaBackup/Balance/Balance_PS_JAK_AureliaPistol',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TortureTruck/Balance_PS_JAK_TortureTruck',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven',
    '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SS_L',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall',
    '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_01_Common',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_01_Common_No_Elemental',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_03_Rare',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/RockNRoll_Intro/Balance_SM_DAL_PlayableIntroOnly',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant',
    '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_02_UnCommon',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane',
    '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer',
    '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_Common',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_FirstGunA',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_FirstGunB',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_02_UnCommon',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_03_Rare',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader',
    '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_02_Uncommon',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/CrazyEarlDefault/Balance_DAL_AR_CrazyEarlDefault',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord',
    '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_01_Common',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_02_UnCommon',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob',
    '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper',
    '/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_01_Common',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_02_Uncommon',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_03_Rare',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_04_VeryRare',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns',
    '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy',
    '/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_01_Common',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_02_UnCommon',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_03_Rare',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_04_VeryRare',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt',
    '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/WardenWeapon/Balance_AR_TOR_Warden',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_01_Common',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_02_Uncommon',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_03_Rare',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_04_VeryRare',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm',
    '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_01_Common',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_02_UnCommon',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_03_Rare',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_04_VeryRare',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending',
    '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ',
    '/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian',
    '/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_01_Common',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_02_Uncommon',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_03_Rare',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_04_VeryRare',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime',
    '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks',
    '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_01_Common',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_02_Uncommon',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_03_Rare',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_04_VeryRare',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor',
    '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher',
    '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker',
    '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand',
    '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker',
    '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger',
    '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux'
]

for bal in wbal_name:
    wbals=Balance.from_data(data, bal)
    mat_type=len(wbals.categories)
    for cat in wbals.categories:
        if cat.index==2:
            for bals in wbal_name:
                wbalslist=Balance.from_data(data, bals)
                for cats in wbalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
            cat.select_multiple=True
            cat.num_min=1
            cat.num_max=3
        if cat.index==mat_type-1:
            for bals2 in wbal_name:
                wbalslist2=Balance.from_data(data, bals2)
                for cats2 in wbalslist2.categories:
                    if len(cats2)!=0:
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        if 'material' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
                        if '_mat_' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
            break
    wbals.hotfix_full(mod)


#Shields

#List the Balances
sbal_name=[
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_04_VeryRare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_04_VeryRare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_01_Common',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_02_Uncommon',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_03_Rare',
    '/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_04_VeryRare',
    '/Game/Gear/Shields/_Design/_Uniques/Aurelia/Balance/InvBalD_Shield_LGD_Aurelia',
    '/Game/Gear/Shields/_Design/_Uniques/BackHam/Balance/InvBalD_Shield_BackHam',
    '/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster',
    '/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole',
    '/Game/Gear/Shields/_Design/_Uniques/BuriedAlive/Balance/InvBalD_Shield_BuriedAlive',
    '/Game/Gear/Shields/_Design/_Uniques/Cyttorak/bALANCE/InvBalD_Shield_Cyttorak',
    '/Game/Gear/Shields/_Design/_Uniques/Dispensary/Balance/InvBalD_Shield_LGD_Dispensary',
    '/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader',
    '/Game/Gear/Shields/_Design/_Uniques/GoldenTouch/Balance/InvBalD_Shield_GoldenTouch',
    '/Game/Gear/Shields/_Design/_Uniques/Impaler/Balance/InvBalD_Shield_LGD_Impaler',
    '/Game/Gear/Shields/_Design/_Uniques/LoopOf4N631/Balance/InvBalD_Shield_HYP_LoopOf4N631',
    '/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup',
    '/Game/Gear/Shields/_Design/_Uniques/MoxxisEmbrace/Balance/InvBalD_Shield_MoxxisEmbrace',
    '/Game/Gear/Shields/_Design/_Uniques/MrCaffeine/Balance/InvBalD_Shield_PAN_MrCaffeine',
    '/Game/Gear/Shields/_Design/_Uniques/NovaBurner/Balance/InvBalD_Shield_LGD_NovaBurner',
    '/Game/Gear/Shields/_Design/_Uniques/Radiate/Balance/InvBalD_Shield_LGD_Radiate',
    '/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger',
    '/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier',
    '/Game/Gear/Shields/_Design/_Uniques/Revengenader/Balance/InvBalD_Shield_LGD_Revengenader',
    '/Game/Gear/Shields/_Design/_Uniques/RoughRider/Balance/InvBalD_Shield_LGD_RoughRider',
    '/Game/Gear/Shields/_Design/_Uniques/ShootingStar/Balance/InvBalD_Shield_LGD_ShootingStar',
    '/Game/Gear/Shields/_Design/_Uniques/SlideKick/Balance/InvBalD_Shield_LGD_SlideKick',
    '/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap',
    '/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer',
    '/Game/Gear/Shields/_Design/_Uniques/Unpaler/Balance/InvBalD_Shield_LGD_Unpaler',
    '/Game/Gear/Shields/_Design/_Uniques/Vamp/Balance/InvBalD_Shield_Legendary_Vamp',
    '/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward',
    '/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot',
    '/Game/PatchDLC/BloodyHarvest/Gear/Shields/_Design/_Unique/ScreamOfPain/Balance/InvBalD_Shield_ScreamOfTerror',
    '/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart',
    '/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover',
    '/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember',
    '/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Initiative/Balance/InvBalD_Shield_Initiative',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch',
    '/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/VoidRift/Balance/InvBalD_Shield_LGD_VoidRift',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Firewall/Balance/InvBalD_Shield_Legendary_Firewall',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/Balance/InvBalD_Shield_Legendary_MEAT',
    '/Game/PatchDLC/Event2/Gear/Shield/_Unique/Wattson/Balance/InvBalD_Shield_Legendary_Wattson'
]

for bal in sbal_name:
    sbals=Balance.from_data(data, bal)
    mat_type=len(sbals.categories)
    for cat in sbals.categories:
        if cat.index==2:
            for bals in sbal_name:
                sbalslist=Balance.from_data(data, bals)
                for cats in sbalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
            cat.select_multiple=True
            cat.num_min=0
            cat.num_max=3
        if cat.index==3:
            for bals2 in sbal_name:
                sbalslist2=Balance.from_data(data, bals2)
                for cats2 in sbalslist2.categories:
                    if (cats2.index==3) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        #check=len(partsplit)-1
                        #i=0
                        #while i < check:
                            #if '/Game' in partsplit[i]:
                        parts_adj=partsplit[1].replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
                            #i=i+1
            cat.select_multiple=True
            cat.num_min=2
            cat.num_max=3
        if cat.index==mat_type-1:
            for bals3 in sbal_name:
                sbalslist3=Balance.from_data(data, bals3)
                for cats3 in sbalslist3.categories:
                    if len(cats3)!=0:
                        parts=cats3.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        if 'material' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
                        if '_mat_' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
            break
    sbals.hotfix_full(mod)


#Grenades

#List the Balances
gbal_name=[
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_01_Common',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_02_Uncommon',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_03_Rare',
    '/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_04_VeryRare',
    '/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion',
    '/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Chupa/Balance/InvBalD_GM_Chupa',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EchoV2/Balance/InvBalD_GM_EchoV2',
    '/Game/Gear/GrenadeMods/_Design/_Unique/EMP/Balance/InvBalD_GM_EMP',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Epicenter/Balance/InvBalD_GM_Epicenter',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball',
    '/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HipHop/Balance/InvBalD_GM_TOR_HipHop',
    '/Game/Gear/GrenadeMods/_Design/_Unique/HunterSeeker/Balance/InvBalD_GM_HunterSeeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/JustDeserts/Balance/InvBalD_GM_JustDeserts',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Kryll/Balance/InvBalD_GM_Kryll',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mogwai/Balance/InvBalD_GM_Mogwai',
    '/Game/Gear/GrenadeMods/_Design/_Unique/MoxiesBosom/Balance/InvBalD_GM_PAN_MoxiesBosom',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Mushroom/Balance/InvBalD_GM_Shroom',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Nagate/Balance/InvBalD_GM_Nagate',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Quasar/Balance/InvBalD_GM_Quasar',
    '/Game/Gear/GrenadeMods/_Design/_Unique/RedQueen/Balance/InvBalD_GM_RedQueen',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/StormFront/Balance/InvBalD_GM_StormFront',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Summit/Balance/InvBalD_GM_Summit',
    '/Game/Gear/GrenadeMods/_Design/_Unique/Surge/Balance/InvBalD_GM_Surge',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToiletBombs/Balance/InvBalD_GM_TOR_ToiletBombs',
    '/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade',
    '/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WidowMaker/Balance/InvBalD_GM_WidowMaker',
    '/Game/Gear/GrenadeMods/_Design/_Unique/WizardOfNOG/Balance/InvBalD_GM_WizardOfNOG',
    '/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness',
    '/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider',
    '/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn',
    '/Game/PatchDLC/Event2/Gear/GrenadeMods/FishSlap/Balance/InvBalD_GM_FishSlap'
]

for bal in gbal_name:
    gbals=Balance.from_data(data, bal)
    mat_type=len(gbals.categories)
    for cat in gbals.categories:
        if cat.index==1:
            for bals in gbal_name:
                gbalslist=Balance.from_data(data, bals)
                for cats in gbalslist.categories:
                    if (cats.index==1) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
        if cat.index==2:
            for bals2 in gbal_name:
                gbalslist2=Balance.from_data(data, bals2)
                for cats2 in gbalslist2.categories:
                    if (cats2.index==2) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        print(part_path)
                        cat.add_part_name(part_path, 1)
        if cat.index==3:
            for bals3 in gbal_name:
                gbalslist3=Balance.from_data(data, bals3)
                for cats3 in gbalslist3.categories:
                    if (cats3.index==3) & (len(cats3)!=0):
                        parts=cats3.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            cat.num_min=0
            cat.num_max=1
        if cat.index==4:
            for bals4 in gbal_name:
                gbalslist4=Balance.from_data(data, bals4)
                for cats4 in gbalslist4.categories:
                    if (cats4.index==4) & (len(cats4)!=0):
                        parts=cats4.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            cat.select_multiple=True
            cat.num_min=2
            cat.num_max=3
        if cat.index==mat_type-1:
            for bals5 in gbal_name:
                gbalslist5=Balance.from_data(data, bals5)
                for cats5 in gbalslist5.categories:
                    if len(cats5)!=0:
                        parts=cats5.str_partlist()
                        partsplit=parts.split('=')
                        parts_adj=partsplit[1]
                        parts_adj=parts_adj.replace(',Weight', '')
                        parts_adjsplit=parts_adj.split('.')
                        part_path=parts_adjsplit[0]
                        if 'material' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
                        if '_mat_' in part_path.lower():
                            print(part_path)
                            cat.add_part_name(part_path, 1)
            break
    gbals.hotfix_full(mod)


#Artifacts

#List the Balances
abal_name=[
    '/Game/Gear/Artifacts/_Design/BalanceDefs/InvBalD_Artifact',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElDragonJr/Balance/InvBalD_Artifact_ElDragonJr',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/ElectricBanjo/Balance/InvBalD_Artifact_ElectricBanjo',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/Grave/Balance/InvBalD_Artifact_Grave',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/PhoenixTears/Balance/InvBalD_Artifact_PhoenixTears',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/RoadWarrior/Balance/InvBalD_Artifact_RoadWarrior',
    '/Game/Gear/Artifacts/_Design/PartSets/Abilities/_Unique/VaultHunterRelic/Balance/InvBalD_Artifact_Relic',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK',
    '/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/Lunacy/Balance/InvBalD_Artifact_Lunacy'
]

for bal in abal_name:
    abals=Balance.from_data(data, bal)
    mat_type=len(abals.categories)
    for cat in abals.categories:
        if cat.index==1:
            for bals in abal_name:
                abalslist=Balance.from_data(data, bals)
                for cats in abalslist.categories:
                    if (cats.index==2) & (len(cats)!=0):
                        parts=cats.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            if cat.enabled is False:
                cat.enabled=True
        if cat.index==2:
            for bals2 in abal_name:
                abalslist2=Balance.from_data(data, bals2)
                for cats2 in abalslist2.categories:
                    if (cats2.index==1) & (len(cats2)!=0):
                        parts=cats2.str_partlist()
                        partsplit=parts.split('=')
                        check=len(partsplit)-1
                        i=0
                        while i < check:
                            if '/Game' in partsplit[i]:
                                parts_adj=partsplit[i].replace(',Weight', '')
                                parts_adjsplit=parts_adj.split('.')
                                part_path=parts_adjsplit[0]
                                print(part_path)
                                cat.add_part_name(part_path, 1)
                            i=i+1
            break
    abals.hotfix_full(mod)


#Class Mods


mod.close()