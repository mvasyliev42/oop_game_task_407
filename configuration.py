from characters import Characters

class Configuration:
    def readconfig(self):
        read = open("config/characters.txt", 'r')
        characters = []
        for i in read:
            divide = i.split(',')
            print(divide)
            character = Characters(divide[0].strip(), divide[1].strip(), float(divide[2].strip()), float(divide[3].strip()), float(divide[4].strip()))
            characters.append(character)
        return characters