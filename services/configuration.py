from basecard import BaseCard


class Configuration:

    def __init__(self, config_characters_file_name="config/characters.txt"):
        self.config_characters_file_name = config_characters_file_name
        self.cards_configs = []

    def readconfig(self):
        read = open(self.config_characters_file_name, 'r')
        for i in read:
            divide = i.split('|')

            self.cards_configs.append({
                "name": divide[0].strip(),
                "description": divide[1].strip(),
                "strength": float(divide[2].strip()),
                "health": float(divide[3].strip()),
                "mana": float(divide[4].strip())
            })

        return self

    def create_card(self):
        for card_config in self.cards_configs:
            yield BaseCard(card_config["name"], card_config["description"], card_config["strength"],
                           card_config["health"], card_config["mana"])
