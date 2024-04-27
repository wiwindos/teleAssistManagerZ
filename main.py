from telebot import TeleBot

TOKEN = ""

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "hi, baby")

bot.infinity_polling()
#haohi