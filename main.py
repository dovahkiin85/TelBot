from ast import Pass
import os
from types import NoneType
from click import command
from telebot import types

import telebot
import redis
#todo : ad menu buttons :)Doen
#todo : add create state :)Done
#todo : userId (chatId) :)Done
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
count = r.get('*')
countLen = 0
user_id = '1116072285'
createState = False

bot = telebot.TeleBot('6267587812:AAEOgErtw18ePxGF6mzFw8ceAEYCD9bRUbU')

li = []

a = r.get('list')


print(a)

c = 0


menu = types.InlineKeyboardMarkup()
menu.add(types.InlineKeyboardButton('Show the commands', callback_data='SHOW_COM'))
menu.add(types.InlineKeyboardButton('Show the list', callback_data='LIST'))
menu.add(types.InlineKeyboardButton('Insert a name into the list', callback_data='CREATE'))

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global createState
    if call.data == 'SHOW_COM':
        bot.send_message(c,'/start')
        bot.send_message(c,'/list')
        bot.send_message(c,'/create')
    elif call.data == 'LIST':
        bot.send_message(c,f'Here is your list my... you know what? my lawyer has advised me not to finish my sentence.\n {a}')
    elif call.data == 'CREATE':
        if createState == False:
            createState = True
            bot.send_message(c,'You can now insert a name into the list my ni... respected gentlemen by typing anything in the chatbox and sending it to me, of course anything that does not start with /.')
        elif createState == True:
            bot.send_message(c,'You are already in create mode genius; USE YOUR KEYBORD TO SEND ME NAMES THAT DONT START WITH /.')
    bot.answer_callback_query(callback_query_id=call.id, text='Sure mate')


def send_menu(chat_id):
    bot.send_message(chat_id, 'Whats up me boy, what do you need me to do for ye?', reply_markup=menu)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    global c
    messageID = message.chat.id
    send_menu(messageID)
    c = message.chat.id



@bot.message_handler(commands=['list'])
def echo_all(message, chat_id=''):
    messageID = message.chat.id
    bot.reply_to(message,f"here be yer list, my dear nigga \n {r.get('list')}")
    print(c)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    global createState
    global c
    if createState == True:
        c = message.chat.id
        bot.reply_to(message, f"{message.text} is the name you have saved, my very respected and dearly loved nigga")
        r.set('name',f'{message.text}')
        li.append(r.get('name'))
        saver = r.get('list')
        for i in li:
            saver = saver + '\n'
            saver = saver + i + f'Created by:{c}'
        r.set('list',saver)
        createState = False
    elif createState == False:
        bot.reply_to(message,'I have absolutely no idea in gods green earth what to do with THAT.\n You should probably turn on create mode or get help by pressing /start')
bot.infinity_polling()
print(li)
