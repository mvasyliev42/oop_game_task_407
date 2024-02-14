from services.configuration import Configuration
import mysql.connector

configuration = Configuration()

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my123456",
  database="game"
)

mycursor = database.cursor()

sql = "INSERT INTO `cards` (name, description, strength, health, manna, skill_name, skill_strength, skill_health, skill_manna) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
configuration.readconfig()
devided = []
for i in configuration.cards_configs:
    devided.append((i['name'], i['description'], i['strength'], i['health'], i['mana'], i['skill']['name'], i['skill']['strength'], i['skill']['health'], i['skill']['mana']))
mycursor.executemany(sql, devided)

database.commit()

print(mycursor.rowcount, "it works")