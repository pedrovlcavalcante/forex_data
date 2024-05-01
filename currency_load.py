import json

with open('currency.json', 'r') as file:
    currency_list = json.load(file)

for currency in currency_list:
    print(currency['symbol'])