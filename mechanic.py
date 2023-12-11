class Mechanics:
    def __init__(self):
        self.characters = []
        self.winner = None

    def set_character(self, character):
        self.characters.append(character)

    def fight_function(self, pers1, pers2):
        self.characters.append(pers1)
        self.characters.append(pers2)
        while self.characters[0].get_helth() > 0 or self.characters[1].get_helth() > 0:
            self.characters[1].helth -= self.characters[0].strength
            print(f"Chracter 1 now has {self.characters[1].get_helth()} helth")
            self.characters[0].helth -= self.characters[1].strength
            print(f"Chracter 0 now has {self.characters[1].get_helth()} helth")
            if self.characters[0].get_helth() <= 0:
                self.winner = self.characters[1]
            elif self.characters[1].get_helth() <= 0:
                self.winner = self.characters[0]
        # if self.character0.get_strength() > self.character1.get_strength():
        #     self.winner = self.character0
        # else:
        #     self.winner = self.character1
    def get_winner(self):
        #self.fight_function()
        return self.winner.get_name()

    @staticmethod
    def print_info(get_winner):
        def wrapper():
            print(f"Переміг: {get_winner()}")
        return wrapper