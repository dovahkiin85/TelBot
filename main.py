import os
from types import NoneType
from click import command

import telebot
import redis
#todo : ad menu buttons
#todo : add create state
#todo : userId (chatId)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
count = r.get('*')
countLen = 0

bot = telebot.TeleBot('1595573797:Yc8Ad1IrD7NqPj2qSXD6DhIEfJGGlcrj1QnedBQe')

li = []
a = r.get('list')
print(a)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Wassup my nigga,yo i need ye name ye get me nigga? insert yer weird-ass name in the text bar, respectfully your nigga. You can also see said weird-ass names py pressing or typing /list")


@bot.message_handler(commands=['list'])
def echo_all(message):

    bot.reply_to(message,f"here be yer list, my dear nigga \n {r.get('list')}")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"{message.text} is the name you have saved, my very respected and dearly loved nigga")
    r.set('name',f'{message.text}')
    li.append(r.get('name'))
    saver = r.get('list')
    for i in li:
        saver = saver + '\n'
        saver = saver + i
    r.set('list',saver)

bot.infinity_polling()
print(li)
