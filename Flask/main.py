from flask import Flask, render_template, jsonify, request
from services.authorisation import Authorisation
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
    mycursor.execute("SELECT users.username, playerwin_id, COUNT(playerwin_id) as countplayerwin FROM game.games LEFT "
                     "JOIN game.users ON game.users.id = game.games.playerwin_id GROUP BY playerwin_id ORDER BY "
                     "countplayerwin DESC;")
    result = mycursor.fetchall()
    resultlist = []
    for i in result:
        resultlist.append({
            "username": i[0],
            "user_id": i[1],
            "count": i[2]
        })
    return jsonify(resultlist)

@app.route('/api/auth',  methods=["POST"])
def auth():
    data = request.json
    authorisation = Authorisation(data["username"], data["password"])
    login_result = authorisation.login()
    return jsonify({"status":True, "data": login_result})

@app.route('/api/profile',  methods=["GET"])
def profile():
    token = request.headers.get("Authorization")
    token = token.split(" ")[1]
    object_auth = Authorisation()
    new_data = object_auth.check_token(token)
    return jsonify({"status": True, "data": new_data})

if __name__ == '__main__':
    app.run(debug=True)