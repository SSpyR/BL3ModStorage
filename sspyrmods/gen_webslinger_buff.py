from bl3hotfixmod import Mod 

mod=Mod('webslinger_buff.txt',
'Buff for Webslinger',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Buffing')
mod.table_hotfix(Mod.PATCH, '',
'/Game/PatchDLC/Takedown2/Gear/Weapons/DataTable_WeaponBalance_Takedown2',
'AR_WebSlinger',
'DamageScale_2_4F6EF14648BA8F2AE9217DAFEA60EE53',
6.7
)
mod.newline()

mod.close()