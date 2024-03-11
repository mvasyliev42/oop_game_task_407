from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/api/rating')
def rating():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="my123456",
        database="game"
    )

    mycursor = database.cursor()
    mycursor.execute("SELECT users.username, playerwin_id, COUNT(playerwin_id) as countplayerwin FROM game.games LEFT JOIN game.users ON game.users.id = game.games.playerwin_id GROUP BY playerwin_id ORDER BY countplayerwin DESC;")
    result = mycursor.fetchall()
    resultlist = []
    for i in result:
        resultlist.append({
            "username": i[0],
            "user_id": i[1],
            "count": i[2]
        })
    return jsonify(resultlist)


if __name__ == '__main__':
    app.run(debug=True)