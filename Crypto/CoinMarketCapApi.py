import json
import requests

def retrieve_data():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    data = json.loads(r.text)
    return data