import requests
import json
from quote import get_currency_list
import pandas as pd

api = 'https://financialmodelingprep.com/api/v3/historical-price-full/'
api_key = '1eOYlhlapz6jrwVzE4TbH67MbRWTfDa4'
params = {'apikey':api_key}

currency_list = get_currency_list()

def save_historical_data(api, params, quote):
    r = requests.get(api+quote, params=params)
    historical = r.json()
    with open('historical_data.json', 'a', encoding='utf-8') as f:
        json.dump(historical, f, ensure_ascii=False, indent=4)

def load_historical_data():
    with open('historical_data.json', 'r') as file:
        historical_data = json.load(file)
    return historical_data

def separate(historical_data, quote):
    return historical_data[0][quote]

#já foi salvo
# for currency in currency_list:
#     quote = currency['symbol']
#     save_historical_data(api, params, quote)
# hd = load_historical_data()
# sepa = separate(hd, quote)
