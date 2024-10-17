# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:40:40 2024

@author: EVOO
"""

from transliterate import to_cyrillic,to_latin
import telebot

TOKEN="7329873547:AAHYcBKaoF_ivVdk-C4Ew4D-9lG4U2D4gMU"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer= "Assalomu aleykum, Xush kelibsiz!"
    answer+= "\nMatn kiriting: "
    bot.reply_to(message,answer)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii() :
        answer=to_cyrillic(msg)
    else:
        answer=to_latin(msg)
    bot.reply_to(message,answer)

bot.infinity_polling()

