import telebot;

bot = telebot.TeleBot('1757118946:AAFlSzDglq6q2Ce5Aro6taTR0N92k3qYtU0')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Привет":
    		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
    		bot.send_message(message.from_user.id, "Напиши привет")
	else:
    		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)