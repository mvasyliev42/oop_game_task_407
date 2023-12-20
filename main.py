import random
from mechanic import Mechanics
from services.configuration import Configuration
from services.players import Players
from services.mechanica.mechanicapc import MechanicaPC
from services.mechanica.mechanicaplayers import MechanicaPlayers


type_game = int(input("Get type game (0 - PC/ 1 - Player): "))


config = Configuration("config/card.conf")

cards = config.readconfig().create_card()
player1 = Players(50, "player1")
player2 = Players(50, "player2")

for i in range(3):
    player1.add_card(random.choice(cards))
    player2.add_card(random.choice(cards))


player1.print_card()
player2.print_card()

if type_game == 0:
    mechanica = MechanicaPC(player1, player2)
else:
    mechanica = MechanicaPlayers(player1, player2)

list = []
for i in range(3):

    mechanica.choose_cards()

    mechanica.fight_function()
    playerwinner = mechanica.check_winner()
    list.append(playerwinner)
    if list.count(player1) > 1:
        print("game winer", playerwinner.name)
        break
    if list.count(player2) > 1:
        print("game winer", playerwinner.name)
        break

    print("round winer", playerwinner.name)
