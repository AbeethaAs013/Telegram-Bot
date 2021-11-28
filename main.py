import os
import telebot

bot = telebot.TeleBot("12321601")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello I'm Abeetha Chat Bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message, "https://youtube.com/channel/UCeSe057QN12yZwx_zm5osqQ")

bot.polling()