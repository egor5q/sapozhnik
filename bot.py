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
db=client.sapozhnik
users=db.users
texts=db.texts


#textss=['Чо тебе блять сказать? Иди нахуй!','Залупа','Хуй моржовый', 'Пизда блять', 'Хуй соси','Блять',
#      'Сука ебал рот блять','Ты долбоеб или как?','Ебло','Сука']


tex=['Чё надо?','Что "Ципра"? Нахуй идите!']

#for ids in textss:
#    texts.update_one({'texts':'mat'},{'$push':{'textlist':ids}})

       
    
@bot.message_handler(commands=['addword'])
def addword(m):
    if m.from_user.id==631027757 or m.from_user.id==441399484:
        x=m.text.split('/addword ')
        x=x[1]
        if x!='':
            texts.update_one({'texts':'mat'},{'$push':{'textlist':x}})
            bot.send_message(m.chat.id, 'Успешно добавлена новая фраза:\n*'+x+'*', parse_mode='markdown')
    else:
        bot.send_message(m.chat.id, 'Ты не мой администратор!')
    
    
@bot.message_handler(commands=['delword'])
def delword(m):
    if m.from_user.id==631027757 or m.from_user.id==441399484:
        x=m.text.split('/delword ')
        x=x[1]
        if x!='':
            try:
                texts.update_one({'texts':'mat'},{'$pull':{'textlist':x}})
                bot.send_message(m.chat.id, 'Успешно удалена фраза:\n*'+x+'*', parse_mode='markdown')
            except:
                bot.send_message(m.chat.id, 'Такой фразы не существует!')
    else:
        bot.send_message(m.chat.id, 'Ты не мой администратор!')
       
@bot.message_handler()
def handlerr(m):
    text=texts.find_one({'texts':'mat'})   
    if len(text['textlist'])>0:
      if 'ципра' in m.text.lower():
        if 'скажи' in m.text.lower():
            bot.send_chat_action(m.chat.id, 'typing')
            t=threading.Timer(3, sendm, args=[m.chat.id, random.choice(text['textlist'])])
            t.start()
        else:
            bot.send_chat_action(m.chat.id, 'typing')
            t=threading.Timer(3, sendm, args=[m.chat.id, random.choice(tex)])
            t.start()    
            
    else:
       bot.send_chat_action(m.chat.id, 'typing')
       t=threading.Timer(3, sendm, args=[m.chat.id,'Да вы охуели! Удалили у меня все фразы, хуй знает теперь, как отвечать...'])
       t.start()
      
            
            

def sendm(id, text):
    bot.send_message(id,text)
            
            
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
