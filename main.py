from flask import Flask
import requests


app = Flask(__name__)





@app.route("/")
def Hearthstone():
    url = 'https://api.hearthstonejson.com/v1/121569/ruRU/cards.collectible.json'
    response = requests.get(url)
    cards = response.json()
    return cards



if __name__ == "__main__":
    app.run(
        debug = True
        )