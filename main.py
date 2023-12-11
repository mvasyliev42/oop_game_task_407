from characters import Characters
from mechanic import Mechanics
from configuration import Configuration

config = Configuration()

heroes = config.readconfig().create_character()

fight = Mechanics()

fight.fight_function(next(heroes), next(heroes))

print(fight.get_winner())
