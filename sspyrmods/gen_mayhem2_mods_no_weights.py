from bl3hotfixmod import Mod 

mod=Mod('mayhem2_mods_no_weights.txt',
'Mayhem 2 No Modifiers',
'SSpyR',
[
    'Turns of modifiers for Mayhem Mode'
],
lic=Mod.CC_BY_SA_40
)

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

mod.close()