import requests
import json
from config import keys, API_URL


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str) -> float:
        if quote == base:  # не введена ли одна и та же валюта?
            raise APIException(f'Нельзя перевести валюту в саму себя')

        try:  # проверка правильности написания первой валюты:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена')

        try:  # и второй валюты
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена')

        try:  # проверка корректности введенного количества и перевод его в тип float
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # # итог: базовая цена валюты * количество:
        # total_base = float(json.loads(r.content)[keys[base]]) * amount
        r = requests.get(API_URL.format(base_ticker, quote_ticker))
        total_base = float(json.loads(r.content)['data'][keys[base]]) * amount
        return total_base


class APIException(Exception):
    ...
