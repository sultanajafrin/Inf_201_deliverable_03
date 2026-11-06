# Quick manual test: simulating a whole battle
from character import Character
from battle import Battle

hero = Character("Hero", hp_max=100, damage=10)
enemy = Character("Enemy", hp_max=35, damage=5)

fight = Battle(hero, enemy)
fight.simulate_battle()

print(hero.hp, enemy.hp)
print(hero.is_alive, enemy.is_alive)