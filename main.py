import telebot
from config import keys, TOKEN
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n \
<имя валюты, цену которой вы хотите узнать><пробел><имя валюты, \
в которой надо узнать цену первой валюты><пробел><количество первой валюты>\n\
Например: доллар рубль 100\n\
Посмотреть список доступных валют:  /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split()  # сначала переносим параметры в список

        if len(values) != 3:  # проверка на число введенных параметров
            raise APIException('Неверное число параметров')

        quote, base, amount = values  # распаковываем список
        quote, base = quote.casefold(), base.casefold()
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в данных:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос:\n{e}')
    else:
        text = f'{amount} {keys[quote]} ({quote}) = {total_base} {keys[base]} ({base})'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
