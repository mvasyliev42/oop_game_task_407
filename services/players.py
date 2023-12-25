class Players:
    def __init__(self, helth, name):
        self.manna = 10
        self.health = helth
        self.name = name
        self.card_list = []

    def add_card(self, card_object):
        self.card_list.append(card_object)

    def print_card(self):
        print(self.name)
        for card in self.card_list:
            print(card.name, card.description, card.strength, card.health, card.manna)
            if card.skill:
                print(f"\t {card.skill_name}, {card.skill_strength}, {card.skill_health}, {card.skill_manna}")
        print()