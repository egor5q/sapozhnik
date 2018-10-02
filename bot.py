# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize


from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)



client1=os.environ['database']
client=MongoClient(client1)
db=client.sergeygame
users=db.users
psw=db.passwords

@bot.message_handler(commands=['newpass'])
def newpass(m):
   if m.from_user.id==m.chat.id:
      if m.chat.id==60727377:
         x=m.text.split('/newpass ')
         if len(x)==2:
            psw.insert_one(createpass(x[1]))
            bot.send_message(m.chat.id, 'Пароль "'+x[1]+'" успешно создан! Всего паролей: '+str(z)

def createpass(p):
   return {'password':p,
          'ids':[],
          'points':0}
  

if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
