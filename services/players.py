class Players:
    def __init__(self, helth, name):
        self.manna = 10
        self.helth = helth
        self.name = name
        self.card_list = []

    def add_card(self, card_object):
        self.card_list.append(card_object)