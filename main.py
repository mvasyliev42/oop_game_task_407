import random
from mechanic import Mechanics
from services.configuration import Configuration
from services.players import Players
from services.mechanica.mechanicapc import MechanicaPC
from services.mechanica.mechanicaplayers import MechanicaPlayers
from services.socket.socketserver import SocketServer
from services.telegram.telegram import *
from services.match import Match


#type_game = int(input("Get type game (0 - PC/ 1 - Player): "))
type_game = 1
socket_server = SocketServer()

config = Configuration("config/card.conf")

cards = config.read_config_database().create_card()
player1 = Players(50, "player1", socket_server.connectPlayer1())

#todo: create game match
match = Match()
socket_server.sendMessagesPlayer1("Set game's name")
games_name = socket_server.recvMessagesPlayer1()
socket_server.sendMessagesPlayer1("Set password")
p1_password = socket_server.recvMessagesPlayer1()
game_id = match.create_game(player1.users[0], games_name, p1_password)
socket_server.sendMessagesPlayer1(f"Game created, id: {game_id}")
socket_server.sendMessagesPlayer1("Waiting for player2...")




player2 = Players(50, "player2", socket_server.connectPlayer2())
socket_server.sendMessagesPlayer2("Set game's id")
games_id = socket_server.recvMessagesPlayer2()
socket_server.sendMessagesPlayer2("Set password")
p2_password = socket_server.recvMessagesPlayer2()
match_data = match.connect_match(player2.users[0], games_id, p2_password)
socket_server.sendMessagesPlayer2(f"You have connected to the game {match_data[4]}")

#todo: insert valid info (id, password)




for i in range(3):
    player1.add_card(random.choice(cards))
    player2.add_card(random.choice(cards))


player1_cards = player1.print_card()
socket_server.sendMessagesPlayer1(player1_cards)
player2_cards = player2.print_card()
socket_server.sendMessagesPlayer2(player2_cards)

socket_server.recvMessagesPlayer1()
socket_server.recvMessagesPlayer2()

if type_game == 0:
    mechanica = MechanicaPC(player1, player2)
else:
    mechanica = MechanicaPlayers(player1, player2)

list = []
for i in range(3):
    print(list)
    mechanica.choose_cards(socket_server, socket_server)

    mechanica.fight_function()
    playerwinner = mechanica.check_winner()
    list.append(playerwinner)
    if list.count(player1) > 1:
        print("game winer", playerwinner.name)
        socket_server.sendMessagesPlayer1(f"game winer {playerwinner.name}")
        socket_server.sendMessagesPlayer2(f"game winer {playerwinner.name}")
        break
    if list.count(player2) > 1:
        print("game winer", playerwinner.name)
        socket_server.sendMessagesPlayer1(f"game winer {playerwinner.name}")
        socket_server.sendMessagesPlayer2(f"game winer {playerwinner.name}")
        break

    print("round winer", playerwinner.name)
    print(list)