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
textstotalk=db.textstotalk



tex=['Чё надо?','Что "Ципра"? Нахуй идите!']


symbollist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы',
            'ь','э','ю','я',' ',',','!','?','#','.','@','"']

       
    
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
    
@bot.message_handler(commands=['addtalk'])
def addword(m):
    if m.from_user.id==631027757 or m.from_user.id==441399484:
        x=m.text.split('/addtalk ')
        x=x[1]
        if x!='':
            textstotalk.update_one({'texts':'mat'},{'$push':{'textlist':x}})
            bot.send_message(m.chat.id, 'Успешно добавлена новая фраза:\n*'+x+'*', parse_mode='markdown')
    else:
        bot.send_message(m.chat.id, 'Ты не мой администратор!')
    
    
@bot.message_handler(commands=['delword'])
def delword(m):
    if m.from_user.id==631027757 or m.from_user.id==441399484:
        x=m.text.split('/delword ')
        if len(x)>1:
          x=x[1]
          if x!='':
            try:
                texts.update_one({'texts':'mat'},{'$pull':{'textlist':x}})
                bot.send_message(m.chat.id, 'Успешно удалена фраза:\n*'+x+'*', parse_mode='markdown')
            except:
                bot.send_message(m.chat.id, 'Такой фразы не существует!')
        else:
            bot.send_message(m.chat.id, 'Неверный формат.')
    else:
        bot.send_message(m.chat.id, 'Ты не мой администратор!')
       
@bot.message_handler(commands=['deltalktext'])
def delword(m):
    if m.from_user.id==631027757 or m.from_user.id==441399484:
        x=m.text.split('/deltalktext ')
        if len(x)>1:
          x=x[1]
          if x!='':
            try:
                textstotalk.update_one({'texts':'mat'},{'$pull':{'textlist':x}})
                bot.send_message(m.chat.id, 'Успешно удалена фраза:\n*'+x+'*', parse_mode='markdown')
            except:
                bot.send_message(m.chat.id, 'Такой фразы не существует!')
        else:
            bot.send_message(m.chat.id, 'Неверный формат.')
    else:
        bot.send_message(m.chat.id, 'Ты не мой администратор!') 
    
    
@bot.message_handler()
def handlerr(m):
  if m.forward_from==None:
    bot.send_message(441399484,'Имя юзера: '+ m.from_user.first_name+'\nТекст сообщения: '+m.text+'\n'+
                     'Айди чата: '+str(m.chat.id))
    txtotalk=textstotalk.find_one({'texts':'mat'})
    text=texts.find_one({'texts':'mat'})   
    if len(text['textlist'])>0:
      if 'ципра' in m.text.lower():
            bot.send_chat_action(m.chat.id, 'typing')
            t=threading.Timer(3, sendm, args=[m.chat.id, random.choice(text['textlist'])])
            t.start()   
      else:
        if m.forward_from==None:
          x=random.randint(1,100)
          if x<=14:
            bot.send_chat_action(m.chat.id, 'typing')
            t=threading.Timer(3, sendm, args=[m.chat.id, random.choice(txtotalk['textlist'])])
            t.start()
          y=random.randint(1,100)
          if y<=10:
              no=0
              for ids in m.text:
                if ids.lower() not in symbols:
                    no=1
              if no==0:
                  textstotalk.update_one({'texts':'mat'},{'$push':{'textlist':m.text}})
                  bot.send_message(441399484,'В список фраз для общения добавлена новая фраза:\n'+m.text+'\n\n#newwords')
                
            
    else:
       bot.send_chat_action(m.chat.id, 'typing')
       t=threading.Timer(3, sendm, args=[m.chat.id,'Да вы охуели! Удалили у меня все фразы, хуй знает теперь, как отвечать...'])
       t.start()
      
            
            

def sendm(id, text):
    bot.send_message(id,text)
            
            
if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
