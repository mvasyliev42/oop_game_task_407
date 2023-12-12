from mechanic import Mechanics
from services.configuration import Configuration

config = Configuration()

heroes = config.readconfig().create_character()

fight = Mechanics()

fight.fight_function(next(heroes), next(heroes))

print(fight.get_winner())



# todo: 1. Створити конфігурацію карт з файлу
# todo: 2. Створити список з карт і роздати по дві карти гравцям.
# todo: 3. Робимо механіку: 1. виставлення карт, 2. Розрахунок результату бою, 3. Перевірка станів гравців
