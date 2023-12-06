class Mechanics:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
        self.winner = None

    def fight_function(self):
        while self.character1.get_helth() > 0 or self.character2.get_helth() > 0:
            self.character2.helth -= self.character1.strength
            print(f"Chracter 2 now has {self.character2.get_helth()} helth")
            self.character1.helth -= self.character2.strength
            print(f"Chracter 1 now has {self.character2.get_helth()} helth")
            if self.character1.get_helth() <= 0:
                self.winner = self.character2
            elif self.character2.get_helth() <= 0:
                self.winner = self.character1
        # if self.character1.get_strength() > self.character2.get_strength():
        #     self.winner = self.character1
        # else:
        #     self.winner = self.character2
    def get_winner(self):
        self.fight_function()
        return self.winner.get_name()

    @staticmethod
    def print_info(get_winner):
        def wrapper():
            print(f"Переміг: {get_winner()}")
        return wrapper