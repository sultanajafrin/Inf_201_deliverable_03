# Items for the battle simulator

from dice import Dice


class Weapon:
    """A weapon with a name and a dice that decides how much damage it deals"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Create a new weapon.

        Args:
            name (str): The name of the weapon, e.g. "Sword".
            damage_dice (Dice): The dice rolled to decide the damage.
        """
        self.name = name
        self.damage_dice = damage_dice # The weapon holds a Dice object inside it.

    def roll_damage(self) -> int:
        """Roll the weapon's dice and return the damage as a whole number."""
        return self.damage_dice.roll()