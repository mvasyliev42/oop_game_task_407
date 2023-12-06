class Characters:
    def __init__(self, name, type, helth, luck, strength):
        self.helth = helth
        self.name = name
        self.type = type
        self.luck = luck
        self.strength = strength

    def get_name(self):
        return self.name

    def get_helth(self):
        if self.type == "magician":
            cofficient = 0.75
        if self.type == "bercerk":
            cofficient = 1.5
        if self.type == "lycar":
            cofficient = 1.2
        return self.helth * cofficient

    def get_strength(self):
        return self.strength