import telebot

bot = telebot.TeleBot('BOT-TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}, Ваш username: {message.from_user.username} Ваше имя: {message.from_user.first_name}, Ваша фамилия: {message.from_user.last_name}')

bot.infinity_polling();
