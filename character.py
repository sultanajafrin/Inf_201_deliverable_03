# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

"""
Characters for a mini RPG battle simulator. 
Contains the character class and its subclass warrior and mage

"""


from items import Weapon
class Character:
    """
    A character in the battle game.
    A character has a name, hit point (HP) and a base damage.
    It can also hold a weapon. HP is kept between 0 and hp_max.
    """

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
            hp_max (int): The most HP the chara ter can have (default = 100)
            damage (int): Damage delt per attack without a weapon (default = 10)
            weapon : The weapon the character holds (default = None, no weapon)
        """
        self.name = name
        self._hp = hp_max  # The underscore means: only the class itself should change this
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon # none means the character fights without a weapon

    def attack(self, target) -> None:
        """
        Attack another character.
        A weapon gives random damage from its dice.
        without a weapon the character deals its fixed base damage
        
        Args: 
            target(character): The character that is attacked.            
            
        """

        if self.weapon is not None:
            damage = self.weapon.roll_damage()  
        else:
            damage = self.damage  
        # we ask the terget to lower its own HP, we never touch target._hp
        target.take_damage(damage)
    
    def take_damage(self, amount: int) -> None:
        """
        Lower this character's pwn HP.
        Args:
            amount(int): How much damage to take. Hp never goes below 0.
        """
        self._hp -= amount
        self._hp = max(self._hp, 0)  # Stops HP from becoming negative 

    def heal(self, amount: int) -> None:
        """
        Raise this character's own HP.

        Args: 
            amount (int): How many HP to restore. HP never goes above hp_max.
        
        """
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  
    
    def introduce(self) -> None:
        """Print a short greeting with the character's name."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Short text for developers, shown when we inspect the object."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """Readable text, shown when we use print() on the object."""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Read-only HP. We can look at it, but not change it directly.
        
        Returns: 
            int: The current hit points.
        """
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only.Tells if the character is still in the fight."""
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
        """
        Take damage after armor has blocked part of it.
        Args:
            amount (int) : The damage before armor is applied.
        """
        # max(..., 0) makes sure weak hits give 0 damage, never negative
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
        """
        Attack with a spell if there is enough mana, otherwise attack normally.
        with at least 10 mana the mage soends 10 and deals double damage. the 
        spell ignors the weapon. with less mana it makes a normal attack and regains 5 mana.
        """
        if self.mana >= 10:
            # Spell: costs 10 mana and deals double damage.
            # It does not use the weapon, only the mage's own damage value.
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            # Resting gives back 5 mana, but never more than the maximum
            self.mana = min(self.mana + 5, self.mana_max)