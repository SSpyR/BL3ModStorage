from bl3hotfixmod import Mod 

mod=Mod('2petstest.txt',
'FL4K 2 Pets',
'SSpyR',
[
    ''
],
lic=Mod.CC_BY_SA_40
)

mod.comment('Test')
mod.reg_hotfix(Mod.PATCH, '',
'/Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/BPBeastmasterComponent.BPBeastmasterComponent_C',
'CharacterSlots',
"""
(
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet
    ),
    (
        /Game/PlayerCharacters/Beastmaster/_Shared/_Design/Character/Augments/PlayerSlot_Pet
    )
)
"""
)