import telebot
import requests
from telebot import types

bot = telebot.TeleBot('6350229764:AAGWlVarulCL_dQEu3t8r3iQkClzqHjqWhc')
API='https://openexchangerates.org/api/latest.json?app_id=c3f10262473f4d57a0b9acfcf2c4fc04&symbols=RUB'
API1=''
@bot.message_handler(commands=['start'])
def starts(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Информация взята с этого сайта', url='https://openexchangerates.org/')
    btn2 = types.InlineKeyboardButton('курс доллара $', callback_data='usd_kurs')
    btn3 = types.InlineKeyboardButton('курс доллара €', callback_data='eur_kurs')
    markup.add(btn1)
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, бот создан для того чтобы узнать курс валют', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'usd_kurs':
        response = requests.get(API)
        data = response.json()
        usd_rate = data['rates'].get('RUB')
        if usd_rate:
            bot.send_message(callback.message.chat.id, f'Вот такой курс доллара к рублю: {usd_rate} 💵')
        else:
            bot.send_message(callback.message.chat.id, 'К сожалению, не удалось получить курс доллара.')
    elif callback.data == 'eur_kurs':
        response = requests.get(API1)
        data = response.json()
        usd_rate = data['rates'].get('RUB')
        bot.send_message(callback.message.chat.id, 'Вот такой курс евро: {')



bot.polling(none_stop=True)
