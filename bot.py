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
db=client.grouphelper
chats=db.chats

@bot.message_handler(commands=['stat'])
def stats(m):
   x=chats.find_one({'id':m.from_user.id})
   if x!=None:
      try:
         bot.send_message(m.chat.id, 'Статистика пользователя в данном чате:\nСообщения: '+str(x['users'][m.from_user.id]['messages'])+'\nМаты: '+str(x['users'][m.from_user.id]['mats']))
      except:
         bot.send_message(m.chat.id, 'Вы еще не отправили в этот чат ни одного сообщения!')
   else:
      bot.send_message(m.chat.id, 'Вы ещё не отправили ни одного сообщения!')



@bot.message_handler(content_types=['text'])
def mats(m):
   chat=chats.find_one({'id':m.chat.id})
   if chat==None:
      print('1')
      chats.insert_one(createchat(m.chat.id))
   chat=chats.find_one({'id':m.chat.id})
   userss=[]
   for ids in chat['users']:
      userss.append(chat['users'][ids]['id'])
   if m.from_user.id not in userss:
      print('2')
      chats.update_one({'id':m.chat.id}, {'$set':{'users.'+str(m.from_user.id):createuser(m.from_user.id, m.from_user.username, m.from_user.first_name)}})
   chats.update_one({'id':m.chat.id}, {'$inc':{'users.'+str(m.from_user.id)+'.messages':1}})
   mat=['хуй', 'пизда', 'пидор', 'мудак', 'залупа', 'блядь', 'блять', 'хуе', 'хуя', 'манда', 'еблан', 'ебан', 'пидр','даун', 'бля']
   x=0
   for ids in mat:
      if ids in m.text.lower():
         x=1
   if x==1:
      chats.update_one({'id':m.chat.id}, {'$inc':{'users.'+str(m.from_user.id)+'.mats':1}})
      texts=['Не ругайся!','Плохо таким быть!', 'У нас здесь не матерятся!', 'Тут приличное общество, не ругайся.', 'Зачем материться?', 'Не надо так.', 'Эй, не матерись!', 'Давай без мата.']
      text=random.choice(texts)
      bot.reply_to(m, text)


def createuser(id, username, name):
   return {'id':id,
           'username':username,
           'name':name,
           'mats':0,
           'messages':0
          }

def createchat(id):
   return {'id':id,
           'users':{}
         
          }


if True:
 try:
   print('7777')
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
       
