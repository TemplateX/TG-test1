print('qq1')
from keep_alive import keep_alive
from pyrogram import Client, filters
import pytz
import datetime
import time
import os
import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
import requests


with open('BabyFile.txt', 'w+') as file:
    file.write('ку-ку1')
my_file = open("BabyFile.txt", "a+")
my_file.write("и еще кое-что!")
my_file.close()

def send_email(message):
    sender = '--YOUR@MAIL.COM'
    #password = str(os.environ['s_gmail_password'])
    password = 'PASSWD' #для ГМАИЛ
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "новости дня"
        server.sendmail(sender, "sender@mail.com", msg.as_string())

        return "Message was sent!)"
    except Exception as _ex:
        return f"{_ex}\nCheck Your logn or psswd"

def load_key():
    return Fernet.generate_key()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

api_id = str(os.environ['s_api_id'])
api_hash = str(os.environ['s_api_hash'])
# session_string = str(os.environ['s_session_string'])
app = Client("my_account", api_id, api_hash)
# app = Client("my_account", session_string=session_string)
print('qq-:')


PUBLIC_FROM = [
    # список пабликов-доноров, откуда бот будет пересылать посты
    'tass_agency',
    'rbc_news',
    'breakingmash',
]

#для почты таймер и складирование новостей
start_time = time.time()
string_to_file_array = []

@app.on_message(filters.chat(PUBLIC_FROM))
def main(Client, message):
    finale = message.text or message.caption
    if finale is None:
      print('-------finale is None!')
      print('Там цитата или что-то ещё')
      print(message.link)
    else:
      a3d509 = str(os.environ['s_a3d509'])
      if finale == a3d509:
          # тут мы должны начать собирать новости
          print('from_bot')
          return 0
          #print(finale)
      
      v5bmq = str(os.environ['s_v5bmq'])

      if finale == v5bmq:
          # тут мы должны ЗАКОНЧИТЬ собирать новости
          print('from_bot')
          #app.send_message(chat_id='hrdshs00rhsge36w2546', text="Бот прислал v5bmq")
          return 0
          
      if message.chat.title is not None:
        tz_moscow = pytz.timezone("Europe/Moscow")
        dt_moscow = str(datetime.datetime.now(tz_moscow).strftime("%d.%m.%Y_%H:%M:%S"))
        MyMessageTitle = message.chat.title
        finale = '#' + str(MyMessageTitle) + ' ' + str(dt_moscow) + '\n\n' + finale
        # aMessageFromNone = message.forward_from_chat.title
        if message.forward_from_chat is not None:
            MyMessageTitle2 = message.forward_from_chat.title
            # finale = str(MyMessageTitle) + '\n' + "Переслал из:" + '\n' + str(MyMessageTitle2) + '\n\n' + finale
            finale = finale + '\n\n' + '- * - * - * - * - * - * -\n' + str(MyMessageTitle) + " Переслал из: " + '#'+ str(
                MyMessageTitle2)
      else:
        print('-------message.chat.title is None')
      print(finale)
      app.send_message(chat_id='hrdshs00rhsge36w2546', text=finale)
      
      global string_to_file_array
      global start_time
      string_to_file_array.append(finale)
      #end_time = time.time()
      if len(string_to_file_array)==1:
          
          start_time = time.time()
      if len(string_to_file_array)>1:
          end_time = time.time()
          
          my_time = round(end_time - start_time)
          print(my_time, len(string_to_file_array))
          finstr = ""
          if (my_time > 900) and (len(string_to_file_array)>10):
          # if (my_time > 180) and (len(string_to_file_array)>2):
              for inarraynews in string_to_file_array:
                  finstr = finstr + '\n\n' + '-–—-–—-–—-–—-–—' + '\n\n' + inarraynews
              print('\n*()*()*()\n\n', finstr, '\n\n*()*()*()\n')
    
              #шифровальщик
              my_str = finstr
              my_file = open("BabyFile.txt", "w+")
              my_file.write(my_str)
              my_file.close()
              #my_file = open("BabyFile.txt", "a+")
              #my_file.write("\n\nи еще кое-что!")
              #my_file.close()
    
              key = load_key()
              file = 'BabyFile.txt'
              # зашифровать файл
              encrypt(file, key)
              with open('BabyFile.txt', 'r+') as file:
                 content = file.read()  # Чтение
                 file.seek(0, 0)  # Переход в начало файла
                 file.write(str(key, encoding='utf-8')[:-1])  # Запись новой строки
                 #-2  # через replace убираю знаки равно
                 content = content.replace('=', "")
                 file.write(content)
              
              with open('BabyFile.txt', 'r+') as file:
                  message = file.read()
              print(message, '\nЩас отправлю это!!')
              send_email(message=message)
              print('отправка - всё')
              #requested_msg = str(message)
              #requested_msg_fin = f'https://api.telegram.org/botНОМЕРБОТА-чат-айди{requested_msg}'
              #requests.get(requested_msg_fin)
              
              start_time = time.time()
              string_to_file_array.clear()

keep_alive()
app.run()  # Automatically start() and idle()
