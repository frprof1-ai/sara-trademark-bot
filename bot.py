import telebot
import requests
from time import sleep

BOT_TOKEN = "TOKEN_HERE"   # توکن را بعدها در تنظیمات قرار می‌دهیم، نه اینجا

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "ربات پایش علائم تجاری فعال است ✅ ")

def main_loop():
    while True:
        # اینجا بعداً سیستم جستجوی 'سا' را اضافه می‌کنیم
        sleep(3600)

if __name__ == "__main__":
    from threading import Thread
    Thread(target=main_loop).start()
    bot.polling()
