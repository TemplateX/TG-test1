print('qq1')
from keep_alive import keep_alive

#telegram
from pyrogram import Client, filters
import pytz
import datetime
import time
# 51.79.229.202:3128
import os

api_id = str(os.environ['s_api_id'])
api_hash = (os.environ['s_api_hash'])
app = Client("my_account", api_id, api_hash)
print('qq:')


PUBLIC_FROM = [
    # список пабликов-доноров, откуда бот будет пересылать посты
    'tass_agency',
    'rbc_news',
    'breakingmash',
    'svtvnews',
    'meduzalive',
    'Ateobreaking',
    'SolovievLive',
    'news_sirena',
    'bbbreaking',
    'rusbrief',
    'yxoydo6si6e7474uf'#Мой скрытый канал
    #"-1002047800128" #Template - мой канал id,
]


@app.on_message(filters.chat(PUBLIC_FROM))
def main(Client, message):
    finale = message.text or message.caption
    if finale is None:
      print('-------finale is None!')
      print('Там цитата или что-то ещё')
      print(message.link)
    else:
      #print(finale)
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


# keep_alive()
app.run()  # Automatically start() and idle()
