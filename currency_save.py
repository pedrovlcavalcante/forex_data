import requests
import json

api = 'https://financialmodelingprep.com/api/v3/symbol/available-forex-currency-pairs'
api_key = '1eOYlhlapz6jrwVzE4TbH67MbRWTfDa4'

params = {'apikey':api_key}
r = requests.get(api, params=params)
currency = r.json()

with open('currency.json', 'w', encoding='utf-8') as f:
    json.dump(currency, f, ensure_ascii=False, indent=4)
