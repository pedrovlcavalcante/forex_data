import requests
from datetime import datetime
import json

def get_currency_list():
    #criar tabela para as cotações
    with open('currency.json', 'r') as file:
        currency_list = json.load(file)
    return currency_list

def get_quote(quote):
    api = 'https://financialmodelingprep.com/api/v3/quote/'+quote
    api_key = '1eOYlhlapz6jrwVzE4TbH67MbRWTfDa4'

    params = {'apikey':api_key}

    r = requests.get(api, params=params)

    info = r.json()[0]

    name = info['name']
    price = info['price']
    timestamp = info['timestamp']

    time = datetime.fromtimestamp(timestamp)

    return name, price, time