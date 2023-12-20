import random
from mechanic import Mechanics
from services.configuration import Configuration
from services.players import Players
from services.mechanica import Mechanica

config = Configuration("config/card.conf")

cards = config.readconfig().create_card()
player1 = Players(50, "player1")
player2 = Players(50, "player2")

for i in range(3):
    player1.add_card(random.choice(cards))
    player2.add_card(random.choice(cards))


player1.print_card()
player2.print_card()

mechanica = Mechanica(player1, player2)
mechanica.choose_cards()

mechanica.fight_function()
playerwinner = mechanica.check_winner()
print(playerwinner.name)

# todo: 1. Створити конфігурацію карт з файлу
# todo: 2. Створити список з карт і роздати по дві карти гравцям.
# todo: 3. Робимо механіку: 1. виставлення карт, 2. Розрахунок результату бою, 3. Перевірка станів гравців
