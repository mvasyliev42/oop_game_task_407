class BaseMechanica:
    def __init__(self, player1, player2):
        self.player1_cards = []
        self.player2_cards = []
        self.player1 = player1
        self.player2 = player2

    def choose_cards(self):
        while True:

            player1_pass = False
            for i, card in enumerate(self.player1.card_list):
                print(i, card.name, card.manna, card.strength)
            print("Enter 100 to pass")
            card_index = self.player1_input()
            if card_index == 100:
                player1_pass = True
            else:
                print("The", self.player1.name, "took the card: ", card_index)
                if self.player1.card_list[card_index].manna <= self.player1.manna:
                    self.set_cards(1, self.player1.card_list[card_index])
                    del self.player1.card_list[card_index]
                else:
                    player1_pass = True

            player2_pass = False
            for i, card in enumerate(self.player2.card_list):
                print(i, card.name, card.manna, card.strength)
            print("Enter 100 to pass")
            card_index2 = self.player2_input()
            if card_index2 == 100:
                player2_pass = True
            else:
                print("The", self.player2.name, "took the card: ", card_index2)
                if self.player2.card_list[card_index2].manna <= self.player2.manna:
                    self.set_cards(2, self.player2.card_list[card_index2])
                    del self.player2.card_list[card_index2]
                else:
                    player2_pass = True
            if player1_pass and player2_pass:
                break


        #todo: 1. створити безкінечний цикл
        #todo: 2. перевіряємо чи вистачає мани для карти, якщо ні, повторюємо вибір
        #todo: 3. реалізуємо можливість пасу, та виходу з вибору карт при двох пасах

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

    def player1_input(self):
        return int(input(f"{self.player1.name}, {self.player1.manna}, choose a card"))

    def player2_input(self):
        return int(input(f"{self.player2.name}, {self.player2.manna}, choose a card"))