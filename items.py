# Items that characters can hold in the battle simulator. For now it only contains the weapon class.

from dice import Dice


class Weapon:
    """
    A weapon with a name and a dice that decides how much damage it deals
    The weapon holds a dice object inside it, so every attack with the weapon gives a random damage.
    
    """

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
        """Roll the weapon's dice to find out how much damage an attack deals.
        
        returns:
            int: A random whole number from 1 up to the number of sides on the weapon's dice.
            
        """
        # The dice class does the rolling, the weapon only passes it on
        return self.damage_dice.roll()