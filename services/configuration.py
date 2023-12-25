from services.cards import Cards
from services.basecard import BaseCard


class Configuration:

    def __init__(self, config_characters_file_name="config/characters.txt"):
        self.config_characters_file_name = config_characters_file_name
        self.cards_configs = []

    def readconfig(self):
        read = open(self.config_characters_file_name, 'r', encoding="UTF-8")
        for i in read:
            divide = i.split('|')

            if len(divide) > 5:
                skill = {
                "name": divide[5].strip(),
                "strength": float(divide[6].strip()),
                "health": float(divide[7].strip()),
                "mana": float(divide[8].strip())
                }
            else:
                skill = False
                
            self.cards_configs.append({
                "name": divide[0].strip(),
                "description": divide[1].strip(),
                "strength": float(divide[2].strip()),
                "health": float(divide[3].strip()),
                "mana": float(divide[4].strip()),
                "skill": skill
            })

        return self

    def create_card(self):
        card_list = []
        for card_config in self.cards_configs:
            object = Cards(card_config["name"], card_config["description"], card_config["strength"], card_config["health"], card_config["mana"])
            if card_config["skill"] != False:
                object.set_skill(card_config["skill"]["name"], card_config["skill"]["strength"], card_config["skill"]["health"], card_config["skill"]["mana"])
            card_list.append(object)
        return card_list