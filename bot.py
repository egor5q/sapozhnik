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
psw=db.passwords



tips=['0']
i=1
while i<21:
   tips.append(os.environ['tip'+str(i)])
   i+=1

@bot.message_handler(commands=['newpass'])
def newpass(m):
   if m.from_user.id==m.chat.id:    
      if m.chat.id==60727377 or m.chat.id==441399484:
         x=m.text.split('/newpass ')
         if len(x)==2:
            z=psw.find({})
            no=0
            for ids in z:
               if ids['password']==x[1]:
                  no=1
            if no==0:
               h=0
               z=psw.find({})
               for idss in z:
                  h+=1
               psw.insert_one(createpass(x[1]))
               bot.send_message(m.chat.id, 'Пароль "'+x[1]+'" успешно создан! Всего паролей: '+str(h+1))
            else:
               bot.send_message(m.chat.id, 'Такой пароль уже существует!')

               
@bot.message_handler(commands=['allpass'])
def allpass(m):
   if m.chat.id==60727377 or m.chat.id==441399484:
      x=psw.find({})
      text='Все пароли:\n'
      for ids in x:
         text+='`'+ids['password']+'`\n'
      bot.send_message(m.chat.id, text, parse_mode='markdown')
               
               
@bot.message_handler(commands=['login'])
def login(m):
   x=m.text.split('/login ')
   if len(x)==2:
     pw=x[1]
     x=psw.find({})
     team=None
     no=0
     for ids in x:
         print('ids')
         if m.from_user.id in ids['ids']:
            no=1
     if no==0:
         x=psw.find({})
         for idss in x:
           print('ids2')
           if idss['password']==pw:
             team=1
             print('yess')
         if team!=None:
            psw.update_one({'password':pw},{'$push':{'ids':m.from_user.id}})
            bot.send_message(m.chat.id, 'Вы успешно вошли в аккаунт!')
         else:
            bot.send_message(m.chat.id, 'Такого пароля не существует!')
     else:
         bot.send_message(m.chat.id, 'Вы уже состоите в одной команде!')
     


   
@bot.message_handler(commands=['alltips'])
def alltips(m):
   x=psw.find({})
   team=None
   for ids in x:
      if m.from_user.id in ids['ids']:
         team=ids
   if team!=None:
      z=0
      text=''
      for ids in team['tips']:
         z+=1
         text+='('+str(z)+'): '+ids+'\n\n'
      bot.send_message(m.chat.id, text)
         
@bot.message_handler(commands=['buy'])
def buyy(m):
   g=psw.find({})
   team=None
   for ids in g:
      if m.from_user.id in ids['ids']:
         team=ids
   if team!=None:
      x=m.text.split('/buy ')
      if len(x)==2:
         try:
           h=int(x[1])
           tip=tips[h]
           if tip not in team['tips']:
             if h!=20:
               cost=5
             else:
               cost=200
             if g['points']>=cost:
               psw.update_one({'password':g['password']},{'$inc':{'points':cost}})
               bot.send_message(m.chat.id, tip+'\n\nОставшиеся очки: '+str(g['points']-cost))
               psw.update_one({'password':team['password']},{'$push':{'tips':tip}})
             else:
               bot.send_message(m.chat.id, 'Недостаточно очков!')
           else:
               bot.send_message(m.chat.id, 'У вас уже куплена эта подсказка!')
         except:
            bot.send_message(m.chat.id, 'Какая-то ошибка. Скорее всего, номер подсказки указан неверно (всего подсказок: 20)')
   else:
    bot.send_message(m.chat.id, 'Вы не состоите ни в одной команде!')
  
   
            
@bot.message_handler(commands=['start'])
def start(m):
 if m.chat.id==m.from_user.id:
   x=psw.find({})
   yes=0
   for ids in x:
      if m.from_user.id in ids['ids']:
         yes=1
   if yes==0:
      bot.send_message(m.chat.id,'Для авторизации введите следующий текст:\n'+
                       '/login *пароль*\nГде *пароль* - выданный вашей команде пароль.')
  
                             
                             
def createpass(p):
   return {'password':p,
          'ids':[],
          'points':0,
          'tips':[]
          } 

helplist={
   1:'',
   2:'',
   3:'',
   4:'',
   5:''
   }
                             
                             

if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
