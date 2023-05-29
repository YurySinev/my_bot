# import requests
# import json
#
# keys = {
#     'доллар': 'USD',
#     'рубль': 'RUB',
#     'евро': 'EUR',
#     'йена': 'JPY',
#     'фунт': 'GBP',
#     'франк': 'CHF',
#     'реал': 'BRL',
#     'крона': 'DKK',
#     'злотый': "PLN"
# }
#
# quote_ticker = keys['доллар']
# base_ticker = keys['рубль']
# r = requests.get(
#     'https://api.freecurrencyapi.com/v1/latest?apikey=0kQyreBorn8mx0llYXO2tSZASpvRaWSB8UkvTVuY&currencies={}&base_currency={}'.format(quote_ticker, base_ticker))
# print(json.loads(r.content)) # {'data': {'CHF': 0.130346}}
# total_base = json.loads(r.content)['data'][quote_ticker]
# print(total_base)
