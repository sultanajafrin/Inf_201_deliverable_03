# Quick manual test: attacking with and without a weapon.

from character import Character
from dice import Dice
from items import Weapon

knight = Character("Knight", weapon=Weapon("Sword", Dice(sides=8)))
peasant = Character("Peasant")

dummy1 = Character("Dummy 1", hp_max=100)
dummy2 = Character("Dummy 2", hp_max=100)

peasant.attack(dummy1)
print(dummy1.hp)

knight.attack(dummy2)
print(dummy2.hp)