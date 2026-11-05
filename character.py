# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon
class Character:
    """Represents a character in the RPG"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Equipped weapon (default = None, no weapon)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()  # Weapon damage comes from a dice roll
        else:
            damage = self.damage  # No weapon: use the default base damage
        target.take_damage(damage)
    
    def take_damage(self, amount: int) -> None:
        """Reduce this character's own HP, never going below 0"""
        self._hp -= amount
        self._hp = max(self._hp, 0)  # HP cannot end up lower than 0    

    def heal(self, amount: int) -> None:
        """Increase this character's own HP, never going above hp_max"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot go above the maximum
    
    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Public read-only property: True if the character has HP left"""
        return self._hp > 0