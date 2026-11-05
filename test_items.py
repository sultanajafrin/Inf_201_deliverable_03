from dice import Dice
from items import Weapon

sword = Weapon("Sword", Dice(sides=8))

print(sword.name)
print(sword.damage_dice)
print(sword.roll_damage())