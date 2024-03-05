class Players:
    def __init__(self, helth, name, users):
        self.manna = 100
        self.health = helth
        self.name = name
        self.card_list = []
        self.users = users
        self.experience = 0

        # todo: set userifno fields

    def set_experience(self, damage):
        self.experience += damage

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

    # todo: set userinfo add method
