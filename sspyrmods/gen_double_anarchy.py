from bl3hotfixmod import Mod 

mod=Mod('double_anarchy.bl3hotfix',
'Changing the name of Light Show to Double Anarchy',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40,
cats='gear-pistol, text'
)

mod.comment('Name Change')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Name_VLA_PS_Lasocannon',
'PartName',
'Double Anarchy'
)
mod.newline()

mod.close()