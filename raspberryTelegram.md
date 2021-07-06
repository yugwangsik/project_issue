# telepot 다운
  - pip3 install telepot
  - pip3 install python-telegram-bot --upgrade

# 텔레그램에서 사진
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'].upper() == 'LED ON':
            bot.sendMessage(chat_id, msg['text'])
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, '지원하지 않는 기능입니다')


TOKEN = 'XXXXXXXXX:XXXXXXXXXXXXXX-XXX_XXXXXXXXXXXXXXXXXXXXXX'    # 텔레그램으로부터 받은 Bot API 토큰

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while True:
    time.sleep(1000)
