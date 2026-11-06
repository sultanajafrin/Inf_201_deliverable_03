# Quick manual test: creating a Warrior

from character import Warrior

conan = Warrior("Conan")
print(conan.armor)
print(conan.hp)

conan.take_damage(12)
print(conan.hp)

conan.take_damage(3)
print(conan.hp)