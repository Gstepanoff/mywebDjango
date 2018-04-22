import telebot
bot = telebot.TeleBot("405049514:AAFwsyg1QhdsnVdCTQFrTvo8QKxj_xRwkn0")
API_TOKEN = '405049514:AAFwsyg1QhdsnVdCTQFrTvo8QKxj_xRwkn0'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Это только начало!
Все, что ты напишешь будет использовано против тебя!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
