# Quick manual test: the mage attacking with spells and normal attacks
from character import Character, Mage

merlin = Mage("Merlin")
dummy = Character("Dummy", hp_max=100)

merlin.attack(dummy)
merlin.attack(dummy)
merlin.attack(dummy)
print(merlin.mana, dummy.hp)

merlin.attack(dummy)
print(merlin.mana, dummy.hp)