# Battle class for the battle simulator 


from character import Character


class Battle:
    """Manages a turn-based fight between a hero and an enemy"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Set up a battle between two characters.

        Args:
            hero (Character): The fighter that attacks first each round.
            enemy (Character): The fighter that hits back.
        """
        # The battle holds both fighters so its methods can use them.
        # Any kind of Character works: Warrior, Mage or a plain Character.
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round: the hero attacks, then the enemy hits back if alive."""
        self.hero.attack(self.enemy)
        # A dead enemy must not get to attack, so we check first
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Play rounds until one of the fighters is no longer alive."""
        # The loop stops as soon as either fighter reaches 0 HP
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()