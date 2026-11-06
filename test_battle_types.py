# Quick manual test: a warrior with a sword against a mage

from character import Warrior, Mage
from dice import Dice
from items import Weapon
from battle import Battle

sword = Weapon("Sword", Dice(sides=8))

knight = Warrior("Knight", weapon=sword)
wizard = Mage("Wizard")

fight = Battle(knight, wizard)
fight.simulate_battle()

print(knight.hp, wizard.hp)
print(knight.is_alive, wizard.is_alive)
print(wizard.mana)