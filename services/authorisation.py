import hashlib

import random
import mysql.connector
class Authorisation():
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my123456",
            database="game"
        )

        self.mycursor = self.database.cursor()
    def login(self):
        self.mycursor.execute("SELECT * FROM `users` WHERE `username`=%s", (self.username,))
        result = self.mycursor.fetchone()
        if result == None:
            return self.registration()
        if self.get_hash_password(self.password) == result[2]:
            return (result[0], self.username, self.get_token(result[0]))
        return False

    def registration(self):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (self.username, self.get_hash_password(self.password))
        self.mycursor.execute(sql, val)
        self.database.commit()
        return (self.mycursor.lastrowid, self.username, self.get_token(self.mycursor.lastrowid))

    def get_hash_password(self, string):
         # Кодування рядка у байти
         encoded_string = string.encode()

         # Створення MD5 хешу
         md5_string = hashlib.md5(encoded_string)

         # Повернення хешу у шістнадцятковому форматі
         return md5_string.hexdigest()

    def get_token(self, user_id):
        token = self.get_hash_password(self.username + "Random Text" + str(random.randint(0, 10000)))
        token = self.get_hash_password(token)
        sql = "INSERT INTO tokens (user_id, token) VALUES (%s, %s)"
        val = (user_id, token)
        self.mycursor.execute(sql, val)
        self.database.commit()
        return token

    def check_token(self, token):
        self.mycursor.execute("SELECT * FROM `tokens` WHERE `token`=%s", (token,))
        result = self.mycursor.fetchone()
        if result != None:
            self.mycursor.execute("SELECT * FROM `users` WHERE `id`=%s", (result[1],))
            result = self.mycursor.fetchone()
            return result
        else:
            result = False