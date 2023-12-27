class BaseMechanica:
    def __init__(self, player1, player2):
        self.player1_cards = []
        self.player2_cards = []
        self.player1 = player1
        self.player2 = player2

    def choose_cards(self, connect1, connect2):
        while True:

            player1_pass = False
            player_messages = ""
            for i, card in enumerate(self.player1.card_list):
                player_messages += f"{i}, {card.name}, {card.manna}, {card.strength} \n"
                # todo: винести в окрему функцію
                if card.skill:
                    player_messages += f"\t {card.skill_name}, {card.skill_strength}, {card.skill_health}, {card.skill_manna} \n"
            player_messages += "Enter 100 to pass \n"
            connect1.sendMessagesPlayer1(player_messages)
            card_index = int(connect1.recvMessagesPlayer1()) #self.player1_input()
            if card_index == 100:
                player1_pass = True
            else:
                print("The", self.player1.name, "took the card: ", card_index)
                if self.player1.card_list[card_index].manna <= self.player1.manna:
                    skill_use = self.player1_input()
                    if skill_use == 1:
                        self.player1.card_list[card_index].skill_use = True
                    self.set_cards(1, self.player1.card_list[card_index])
                    del self.player1.card_list[card_index]
                else:
                    player1_pass = True

            player2_pass = False
            player_messages = ""
            for i, card in enumerate(self.player2.card_list):
                player_messages += f"{i}, {card.name}, {card.manna}, {card.strength} \n"
                # todo: винести в окрему функцію
                if card.skill:
                    player_messages += f"\t {card.skill_name}, {card.skill_strength}, {card.skill_health}, {card.skill_manna} \n"
            player_messages += "Enter 100 to pass \n"
            connect2.sendMessagesPlayer2(player_messages)
            card_index = int(connect2.recvMessagesPlayer2()) #self.player2_input()
            if card_index == 100:
                player2_pass = True
            else:
                print("The", self.player2.name, "took the card: ", card_index)
                if self.player2.card_list[card_index].manna <= self.player2.manna:
                    skill_use = self.player2_input()
                    if skill_use == 1:
                        self.player2.card_list[card_index].skill_use = True
                    self.set_cards(2, self.player2.card_list[card_index])
                    del self.player2.card_list[card_index]
                else:
                    player2_pass = True
            if player1_pass and player2_pass:
                break


    def set_cards(self, player, card):
        if player == 1:
            self.player1_cards.append(card)
            self.player1.manna -= card.manna
        else:
            self.player2_cards.append(card)
            self.player2.manna -= card.manna

    def fight_function(self):
        player1_card_attack = 0
        player1_card_protection = 0
        player2_card_attack = 0
        player2_card_protection = 0
        for i in self.player1_cards:
            if i.skill_use == True:
                player1_card_attack += i.skill_strength
                player1_card_protection += i.skill_health
            player1_card_attack += i.strength
            player1_card_protection += i.health
        for j in self.player2_cards:
            if j.skill_use == True:
                player2_card_attack += j.skill_strength
                player2_card_protection += j.skill_health
            player2_card_attack += j.strength
            player2_card_protection += j.health

        damage1 = player1_card_attack - player2_card_protection
        damage2 = player2_card_attack - player1_card_protection

        self.player1.health -= damage2
        self.player2.health -= damage1

    def check_winner(self):
        if self.player1.health > self.player2.health:
            return self.player1

        elif self.player1.health == self.player2.health:
            return True

        else:
            return self.player2

    def player1_input(self):
        return int(input(f"{self.player1.name}, {self.player1.manna}, choose a card"))

    def player2_input(self):
        return int(input(f"{self.player2.name}, {self.player2.manna}, choose a card"))