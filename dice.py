# A dice class that makes damage random in the battle simulator.


import random


class Dice:
    """
    A dice with any number of sides. A dice with n sides gives a random whole number 
    from 1 to n when it is rolled. it can be rolled with roll() or by calling it, e.g d20()
    
    """

    def __init__(self, sides: int = 6) -> None:
        """
        Create a new dice.

        Args:
            sides (int): Number of sides on the dice (default = 6, minimum = 2)

        Raises:
            ValueError: If sides is less than 2
        """
        if sides < 2:
            # A dice with fewer than 2 sides makes no sense, so we stop here.
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a number from 1 to sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object, e.g. Dice(sides=6)"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Let us roll the dice by calling it, so d20() does the same as d20.roll()."""
        # We reuse roll(), so the rolling logic lives in only one place
        return self.roll()