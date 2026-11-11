# Battle class for the battle simulator 
# A battle class that runs a turn-based fight between two character.


from character import Character


class Battle:
    """Manages a turn-based fight between a hero and an enemy.
    The hero attacks first in every round. Any kind of character can fight, 
    for example a warrior, a mage or a plain character.
    
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Set up a battle between two characters.

        Args:
            hero (Character): The fighter that attacks first in each round.
            enemy (Character): The fighter that attacks back if it survives.
        """
        # We save both fighters on self so every method can use them.
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play one round of the battle.
        The hero attacks the enemy. If the enemy is still alive afterwards,
        it attacks the hero. A dead enemy does not get a trun.

        """
        self.hero.attack(self.enemy)
        # A dead enemy must not get to attack, so we check first
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """
        Play rounds until one of the fighters is no longer alive.
        After this method has finished, at least one of the characters has 0 HP.

        """
        # "and" means both must be alive, so the first death ends the loop.
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()