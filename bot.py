import telebot
import requests
from bs4 import BeautifulSoup
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
seen_file = "seen.txt"

if not os.path.exists(seen_file):
    open(seen_file, "w").close()

def load_seen():
    with open(seen_file, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

def save_seen(seen):
    with open(seen_file, "w", encoding="utf-8") as f:
        f.write("\n".join(seen))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ ربات فعال است و هر 3 ساعت علائم دارای «سا» را بررسی می‌کند.")

def check_trademarks():
    url = "https://ipm.ssaa.ir/Issue-IssueTrademark?page=1"
    response = requests.get(url, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    seen = load_seen()

    items = soup.select(".issueTrademarkList .row div:nth-child(2)")  # استخراج نام‌ها

    for item in items:
        name = item.get_text(strip=True)
        if "سا" in name and name not in seen:
            bot.send_message(
                chat_id=5465486117,
                text=f"🔔 علامت جدید یافت شد:\n\n**{name}**\n\nℹ️ لینک جستجو:\n{url}",
                parse_mode="Markdown"
            )
            seen.add(name)

    save_seen(seen)

def main_loop():
    while True:
        check_trademarks()
        time.sleep(10800)  # هر 3 ساعت

if __name__ == "__main__":
    main_loop()
