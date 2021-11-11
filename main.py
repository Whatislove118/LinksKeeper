import telebot

from core import *

bot = telebot.TeleBot(BOT_KEY)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, GREETING_MESSAGE)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Hello':
        bot.send_message(message.from_user.id, 'Sup bro')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'HELP??')

bot.polling(none_stop=True, interval=0)
