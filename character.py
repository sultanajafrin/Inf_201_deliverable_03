# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon
class Character:
    """Represents a character in our mini RPG battle game"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        """
        Create a new character.

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Equipped weapon (default = None, no weapon)
        """
        self.name = name
        self._hp = hp_max  # The underscore means: only the class itself should change this
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon # none means the character fights without a weapon

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()  # Weapon damage comes from a dice roll
        else:
            damage = self.damage  # No weapon, so use the normal damage
        target.take_damage(damage) # We ask the target to lower its own HP
    
    def take_damage(self, amount: int) -> None:
        """Reduce this character's own HP, never going below 0"""
        self._hp -= amount
        self._hp = max(self._hp, 0)  # HP cannot end up lower than 0    

    def heal(self, amount: int) -> None:
        """Increase this character's own HP, never going above hp_max"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot go above the maximum
    
    def introduce(self) -> None:
        """Print a short greeting with the character`s name"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Short text for developers, shown when we inspect the object."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """Readable text, shown when we use print() on the object."""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Read-only HP. We can look at it, but not change it directly."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only.True while the character has more than 0 HP."""
        return self._hp > 0

class Warrior(Character):
    """A defensive character: armor blocks part of every hit it receives"""

    def __init__(self, name, hp_max=100, damage=10, weapon=None, armor=5):
        """
        Create a new warrior.

        Args:
            name: The name of the warrior.
            hp_max: The most HP the warrior can have (default = 100).
            damage: Damage dealt per attack without a weapon (default = 10).
            weapon: The weapon the warrior holds, or None (default = None).
            armor: How much damage is blocked per hit (default = 5).
        """
        # Character already knows how to set up name, HP, damage and weapon,
        # so we hand that part over instead of writing it again
        super().__init__(name, hp_max, damage, weapon)
        # The only new thing a warrior has compared to a normal character
        self.armor = armor

    def take_damage(self, amount):
        """Reduce the incoming damage by armor, then take what is left."""
        # max(..., 0) makes sure weak hits give 0 damage, never negative
        # damage (which would heal the warrior by mistake)
        reduced = max(amount - self.armor, 0)
        # Character.take_damage lowers the HP and keeps it at 0 or above
        super().take_damage(reduced)


class Mage(Character):
    """A character that fights with spells, which cost mana"""

    def __init__(self, name, hp_max=100, damage=10, weapon=None, mana=30, mana_max=30):
        """
        Create a new mage.

        Args:
            name: The name of the mage.
            hp_max: The most HP the mage can have (default = 100).
            damage: Damage of a normal attack without a weapon (default = 10).
            weapon: The weapon the mage holds, or None (default = None).
            mana: The mana the mage has right now (default = 30).
            mana_max: The most mana the mage can have (default = 30).
        """
        # Let Character set up name, HP, damage and weapon
        super().__init__(name, hp_max, damage, weapon)
        # The two new things a mage has: mana now, and the maximum
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target):
        """Cast a spell if there is enough mana, otherwise attack normally."""
        if self.mana >= 10:
            # Spell: costs 10 mana and deals double damage.
            # It does not use the weapon, only the mage's own damage value.
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            # Not enough mana: do a normal attack. Character.attack uses
            # the weapon if the mage has one.
            super().attack(target)
            # Resting gives back 5 mana, but never more than the maximum
            self.mana = min(self.mana + 5, self.mana_max)