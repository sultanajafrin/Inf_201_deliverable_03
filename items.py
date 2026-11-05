from dice import Dice


class Weapon:
    """Represents a weapon that deals random damage using a dice"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The dice rolled to decide the damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's dice and return the damage"""
        return self.damage_dice.roll()