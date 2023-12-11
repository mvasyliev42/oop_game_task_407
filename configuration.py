from characters import Characters

class Configuration:

    def __init__(self, config_characters_file_name="config/characters.txt"):
        self.config_characters_file_name = config_characters_file_name
        self.characters = []

    def readconfig(self):
        read = open(self.config_characters_file_name, 'r')
        for i in read:
            divide = i.split(',')

            self.characters.append({
                "name": divide[0].strip(),
                "type": divide[1].strip(),
                "helth": float(divide[2].strip()),
                "luck": float(divide[3].strip()),
                "strength": float(divide[4].strip())
            })

        return self

    def create_character(self):
        for character in self.characters:
            yield Characters(character["name"], character["type"], character["helth"], character["luck"], character["strength"])