import yadisk
import sys
import requests

def telegram_bot_sendtext(bot_message):

   bot_token = '1757118946:AAFlSzDglq6q2Ce5Aro6taTR0N92k3qYtU0'
   bot_chatID = '-1001196305879'
   params = {
    "chat_id": bot_chatID,
    "text": bot_message,
    "parse_mode": "HTML",
   }
   response = requests.get(
    "https://api.telegram.org/bot{}/sendMessage".format(bot_token),
    params=params
   )
   return response.json()

y = yadisk.YaDisk(token="AQAAAAAFzz4bAAcWVJNhoT1G1E81liY-xuEtyr0")
y.mkdir("/Hello Word") # Создать папку
y.upload(sys.argv[1], "/Hello Word/" + sys.argv[1]) # Загружает первый файл
link = y.get_download_link("/Hello Word/" + sys.argv[1])
link = link.replace('&', '&amp;')
print(telegram_bot_sendtext('<a href=\"' + link +'\"> Download  your build </a>'))