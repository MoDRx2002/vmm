from telebot import TeleBot
import os
from api import get_gpt_reply

from keep_alive import keep_alive
keep_alive()



BOT_TOKEN = os.environ['BOT_TOKEN']
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def on_start(message):
    chat_id = message.chat.id
    text = ' مرحبا بك في بوت التيليجرام الخاص ب golden nurese team'
    bot.send_message(chat_id, text)
    return


@bot.message_handler()
def on_message(message):
    chat_id = message.chat.id
    prompt = message.text[:250]
    text = get_gpt_reply(prompt,1000)
    bot.send_message(chat_id, text)


bot.remove_webhook()



bot.infinity_polling()
