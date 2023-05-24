import requests
import json

keys = {
    'доллар': 'USD',
    'рубль': 'RUB',
    'евро': 'EUR',
    'йена': 'JPY',
    'фунт': 'GBP',
    'франк': 'CHF',
    'реал': 'BRL',
    'крона': 'DKK',
    'злотый': "PLN"
}

quote = 'CHF'
base = 'DKK'
r = requests.get(
    f'https://api.freecurrencyapi.com/v1/latest?apikey=0kQyreBorn8mx0llYXO2tSZASpvRaWSB8UkvTVuY&currencies={quote}&base_currency={base}')
# print(json.loads(r.content)) # {'data': {'CHF': 0.130346}}
total_base = json.loads(r.content)['data'][quote]
print(total_base)
# 0.130346
