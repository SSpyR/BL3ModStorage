from bl3hotfixmod import Mod 

mod=Mod('skill_replacement_test.txt',
'Skill Replacement Test',
'SSpyR',
[
    'Test mod to see if I can rearrange skills.'
],
lic=Mod.CC_BY_SA_40
)

#'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Passives/BrawlTree/DoUntoOthers/PassiveSkill_Siren_DoUntoOthers',
#'PassiveSkill_Siren_DoUntoOthers_C',

#Still havent figured this out, ask #bl3-modding about it

mod.comment('Swapping')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_1.Items_OakPlayerAbilityTreeItemData_Ability',
'AbilityClass',
'/Game/PlayerCharacters/Gunner/_Shared/_Design/Passives/_Tree_BottomlessMags/MatchedSet/Passive_Gunner_MatchedSet'
)
mod.newline()

mod.comment('Swapping')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_1.Items_OakPlayerAbilityTreeItemData_Ability',
'AbilityClass',
'Passive_Gunner_MatchedSet_C'
)
mod.newline()

mod.comment('Swapping')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/SirenBrawler/_Shared/_Design/Character/Inventory/AbilityTree_Siren_Brawl:Tiers_OakPlayerAbilityTreeTierData_1.Items_OakPlayerAbilityTreeItemData_Ability',
'MaxPoints',
10
)
mod.newline()

mod.close()