class Players:
    def __init__(self, helth, name):
        self.manna = 100
        self.health = helth
        self.name = name
        self.card_list = []

    def add_card(self, card_object):
        self.card_list.append(card_object)

    def print_card(self):
        message = ""
        message += self.name + "\n"
        for card in self.card_list:
            message += f"{card.name}, {card.description}, {card.strength}, {card.health}, {card.manna}" + "\n"
            if card.skill:
                message += f"\t {card.skill_name}, {card.skill_strength}, {card.skill_health}, {card.skill_manna}" + "\n"
        message += "\n"
        return message