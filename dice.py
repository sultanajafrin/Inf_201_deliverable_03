import random


class Dice:
    """Represents an n-sided dice"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides on the dice (default = 6, minimum = 2)

        Raises:
            ValueError: If sides is less than 2
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a number from 1 to sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object, e.g. Dice(sides=6)"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allow the dice to be rolled by calling it: d20()"""
        return self.roll()