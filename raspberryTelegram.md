# telepot, telegram 다운
  - pip3 install telepot
  - pip3 install python-telegram-bot --upgrade

# 텔레그램에 'P'를 입력하면 사진찍어서 보내주기
```
import time
import telepot
import telegram
import os, sys

from telepot.loop import MessageLoop

photo = "raspistill -o test.jpg"
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'].upper() == 'P':
            os.system(photo)
            botP.send_photo(chat_id, photo=open('test.jpg', 'rb'))
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, 'Unsupported features')


TOKEN = 'XXXXXXXXX:XXXXXXXXXXXXXX-XXX_XXXXXXXXXXXXXXXXXXXXXX'    // 텔레그램으로부터 받은 Bot API 토큰

bot = telepot.Bot(TOKEN)
botP = telegram.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while True:
    time.sleep(1000)
```

# telegram에서 사용자에게 사진 전송
```
import telegram

TOKEN = 'XXXXXXXXX:XXXXXXXXXXXXXX-XXX_XXXXXXXXXXXXXXXXXXXXXX'    // 텔레그램으로부터 받은 Bot API 토큰
botP.send_photo(chat_id, photo=open('test.jpg', 'rb')) // 사용자 ID확인필요 & 사진 경로 확인
```
