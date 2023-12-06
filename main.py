from characters import Characters
from mechanic import Mechanics
from configuration import Configuration

# character1 = Characters("Gendalf", "magician", 100, 50, 200)
# character2 = Characters("Gloria", "bercerk", 100, 35, 150)

config = Configuration()
heroes = config.readconfig()

fight = Mechanics(heroes[0], heroes[1])
print(fight.get_winner())
