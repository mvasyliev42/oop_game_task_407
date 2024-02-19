import hashlib

import mysql.connector
class Authorisation():
    def __init__(self, username, password):
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
            return (result[0], self.username)
        return False

    def registration(self):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (self.username, self.get_hash_password(self.password))
        self.mycursor.execute(sql, val)
        self.database.commit()
        return (self.mycursor.lastrowid, self.username)

    def get_hash_password(self, string):
         # Кодування рядка у байти
         encoded_string = string.encode()

         # Створення MD5 хешу
         md5_string = hashlib.md5(encoded_string)

         # Повернення хешу у шістнадцятковому форматі
         return md5_string.hexdigest()
