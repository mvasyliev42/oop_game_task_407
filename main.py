import random
from mechanic import Mechanics
from services.configuration import Configuration
from services.players import Players
from services.mechanica.mechanicapc import MechanicaPC
from services.mechanica.mechanicaplayers import MechanicaPlayers
from services.socket.socketserver import SocketServer
# from services.telegram.telegram import *
from services.match import Match
import threading
from services.socket.serversockettreads import ServerSocketTreads
import time






def game_logic():

    global match
    global connect_player1

    config = Configuration("config/card.conf")

    socket_server = ServerSocketTreads()

    cards = config.read_config_database().create_card()
    game_id = games_id_list.pop(0)
    player1 = games[game_id]["player1"]
    socket_server.connectPlayer1(games[game_id]["connect1"])
    #todo Create new object sendMessages to connectPlayer1
    socket_server.sendMessagesPlayer1("Waiting for player2...")


    #todo: wait player 2
    while True:
        time.sleep(1)
        if (games[game_id]["connect2"]) != False:
            break
    

    player2 = games[game_id]["player2"]
    socket_server.connectPlayer2(games[game_id]["connect2"])







    for i in range(3):
        player1.add_card(random.choice(cards))
        player2.add_card(random.choice(cards))


    player1_cards = player1.print_card()
    socket_server.sendMessagesPlayer1(player1_cards)
    player2_cards = player2.print_card()
    socket_server.sendMessagesPlayer2(player2_cards)

    #todo: set info for start match
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

        # playerwinner = mechanica.check_winner()

        # list.append(playerwinner)

        if player1.health <= 0 and player2.health <= 0:
            socket_server.sendMessagesPlayer1(f"game winner: draw")
            socket_server.sendMessagesPlayer2(f"game winner: draw")

        elif player1.health <= 0:
            socket_server.sendMessagesPlayer1(f"game winner Player2")
            socket_server.sendMessagesPlayer2(f"game winner Player2")
            match.set_winner_match(player2.users[0], game_id)
            break

        if player2.health <= 0:
            socket_server.sendMessagesPlayer1(f"game winner Player1")
            socket_server.sendMessagesPlayer2(f"game winner Player1")
            match.set_winner_match(player1.users[0], game_id)
            break

        player1.use_experience(socket_server)
        player2.use_experience(socket_server)

        #todo: use exps
        player1.use_experience(connect_player1)
        

        def use_experience(self, connect):
            connect.send(f"У вас є така кількість атрибутів: {self.manna} ,{self.health}, {self.experience}")
            connect.send("Скільки ти хочеш перевести на ману?: ")
            use_count_experience = connect.recv()
            self.experience -= use_count_experience
            self.manna += use_count_experience
            connect.send("Скільки ти хочеш перевести на здоров'є?: ")
            use_count_health = connect.recv()
            self.experience -= use_count_health
            self.manna += use_count_health

        print(list)


# https://miro.com/app/board/uXjVNpJL0N4=/?share_link_id=374435639510

#type_game = int(input("Get type game (0 - PC/ 1 - Player): "))
type_game = 1
socket_server = SocketServer()

games = {}
games_id_list = []


while True:
    users = socket_server.connectPlayer()

    socket_server.sendMessagesPlayer("Choose action: Write 1 - to Create new game; Write 2 - to Connect to the game")
    recieve_message = socket_server.recvMessagesPlayer()
    if recieve_message == '1':
        player1 = Players(50, "player1", users)
        match = Match()
        socket_server.sendMessagesPlayer("Set game's name")
        games_name = socket_server.recvMessagesPlayer()
        socket_server.sendMessagesPlayer("Set password")
        p1_password = socket_server.recvMessagesPlayer()
        game_id = match.create_game(player1.users[0], games_name, p1_password)
        socket_server.sendMessagesPlayer(f"Game created, id: {game_id}")
        games[game_id] = {
            "game_id": game_id,
            "connect1": socket_server.get_connect(),
            "connect2": False,
            "player1": player1,
            "player2": False,
            "password": p1_password,
            "game_name": games_name
        }
        games_id_list.append(game_id)
        thread = threading.Thread(target=game_logic)
        thread.start()
    if recieve_message == '2':
        player2 = Players(50, "player2", users)
        games_name = socket_server.sendMessagesPlayer("Set game's id")
        games_id = int(socket_server.recvMessagesPlayer())
        password = socket_server.sendMessagesPlayer("Set password")
        password1= socket_server.recvMessagesPlayer()
        match = Match()
        match_data = match.connect_match(player2.users[0], games_id, password1)
        if match_data != False:
             games[games_id]["connect2"] = socket_server.get_connect()
             games[games_id]["player2"] = player2




    #todo: Check game activity

    #todo: Set connect info in data