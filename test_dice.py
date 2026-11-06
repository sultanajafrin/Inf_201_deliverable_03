# Quick manual test: creating a dice and the minimum of 2 sides.

from dice import Dice

d2 = Dice(sides=2)
print(d2)

bad_dice = Dice(sides=1)
print("This line is never reached")