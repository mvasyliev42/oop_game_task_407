from mechanic import Mechanics
from services.configuration import Configuration
from services.players import Players

config = Configuration("config/card.conf")

cards = config.readconfig().create_card()
player1 = Players(50, "player1")
player2 = Players(50, "player2")

player1.add_card(next(cards))
player1.add_card(next(cards))
player2.add_card(next(cards))
player2.add_card(next(cards))

player1.print_card()
player2.print_card()

# todo: 1. Створити конфігурацію карт з файлу
# todo: 2. Створити список з карт і роздати по дві карти гравцям.
# todo: 3. Робимо механіку: 1. виставлення карт, 2. Розрахунок результату бою, 3. Перевірка станів гравців
