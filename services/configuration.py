from services.cards import Cards
from services.basecard import BaseCard
import mysql.connector


class Configuration:

    def __init__(self, config_characters_file_name="config/card.conf"):
        self.config_characters_file_name = config_characters_file_name
        self.cards_configs = []

    def readconfig(self):
        read = open(self.config_characters_file_name, 'r', encoding="UTF-8")
        for i in read:
            divide = i.split('|')
            self.add_card_config(divide)

        return self

    def create_card(self):
        card_list = []
        for card_config in self.cards_configs:
            object = Cards(card_config["name"], card_config["description"], card_config["strength"], card_config["health"], card_config["mana"])
            if card_config["skill"] != False:
                object.set_skill(card_config["skill"]["name"], card_config["skill"]["strength"], card_config["skill"]["health"], card_config["skill"]["mana"])
            card_list.append(object)
        return card_list
    def add_card_config(self, divide):
        if len(divide) > 5:
            skill = {
                "name": divide[6],
                "strength": float(divide[6]),
                "health": float(divide[7]),
                "mana": float(divide[8])
            }
        else:
            skill = False

        self.cards_configs.append({
            "name": divide[0],
            "description": divide[1],
            "strength": float(divide[2]),
            "health": float(divide[3]),
            "mana": float(divide[4]),
            "skill": skill
        })
    def read_config_database(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my123456",
            database="game"
        )
        _cursor = mydb.cursor()

        _cursor.execute("SELECT * FROM `cards`")
        result = _cursor.fetchall()
        for i in result:
            i = list(i)
            i.pop(0)
            self.add_card_config(i)
        return self