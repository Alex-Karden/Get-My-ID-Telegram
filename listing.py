import telebot

bot = telebot.TeleBot('BOT-TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'  Ваш ID:  {message.from_user.id}')

bot.infinity_polling();
