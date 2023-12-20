class Mechanica:
    def __init__(self, player1, player2):
        self.player1_cards = []
        self.player2_cards = []
        self.player1 = player1
        self.player2 = player2

    def choose_cards(self):
        for _ in range(1):
            for i, card in enumerate(self.player1.card_list):
                print(i, card.name)
            card_index = int(input(f"{self.player1.name}, choose a card"))
            self.set_cards(1, self.player1.card_list[card_index])
            for i, card in enumerate(self.player2.card_list):
                print(i, card.name)
            card_index2 = int(input(f"{self.player2.name}, choose a card"))
            self.set_cards(2, self.player2.card_list[card_index2])


    def set_cards(self, player, card):
        if player == 1:
            self.player1_cards.append(card)
        else:
            self.player2_cards.append(card)

    def fight_function(self):
        player1_card_attack = 0
        player1_card_protection = 0
        player2_card_attack = 0
        player2_card_protection = 0
        for i in self.player1_cards:
            player1_card_attack += i.strength
            player1_card_protection += i.health
        for j in self.player2_cards:
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