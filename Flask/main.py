from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/api/rating')
def rating():

    return jsonify({"name": None})


if __name__ == '__main__':
    app.run(debug=True)