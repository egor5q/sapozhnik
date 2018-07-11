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


@bot.message_handler(content_types=['text'])
def mats(m):
   mat=['хуй', 'пизда', 'пидор', 'мудак', 'залупа', 'блядь', 'блять', 'хуе', 'хуя', 'манда']
   x=0
   for ids in mat:
      if ids in m.text:
         x=1
   if x==1:
      texts=['Не ругайся!','Плохо таким быть!', 'У нас здесь не матерятся!', 'Тут приличное общество, не ругайся.', 'Зачем материться?', 'Не надо так.']
      text=random.choice(texts)
      bot.reply_to(m.chat.id, m.message_id, text)




if True:
 try:
   print('7777')
   bot.send_message(-1001208357368, 'Бот был перезагружен!')
   bot.polling(none_stop=True,timeout=600)
 except (requests.ReadTimeout):
        print('!!! READTIME OUT !!!')           
        bot.stop_polling()
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except (requests.exceptions.ConnectionError):
            time.sleep(1)
   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(0.1)
       
