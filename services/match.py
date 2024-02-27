import mysql.connector

class Match:

    def __init__(self):
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my123456",
            database="game"
        )

        self.mycursor = self.database.cursor()

    def create_game(self, player1_id, name, password):
        sql = "INSERT INTO games (player1_id, name, password) VALUES (%s, %s, %s)"
        val = (player1_id, name, password)
        self.mycursor.execute(sql, val)
        self.database.commit()
        return self.mycursor.lastrowid

    def connect_match(self, player2_id, match_id, password):
        self.mycursor.execute("SELECT * FROM `games` WHERE `id`=%s AND `password`=%s", (match_id, password,))
        result = self.mycursor.fetchone()
        print(result)
        if result == None:
            return False
        sql = "UPDATE games SET player2_id=%s WHERE id=%s"
        val = (player2_id, match_id,)
        self.mycursor.execute(sql, val)
        self.database.commit()
        print('update')
        return result