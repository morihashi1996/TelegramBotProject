from datetime import datetime

from pycoingecko import CoinGeckoAPI
from telebot import TeleBot

BOT_TOKEN = '5429168277:AAFJyQ5Wg34ERJcf2pf6DaRPeYPVLzR-l2U'

bot = TeleBot(token=BOT_TOKEN)
coin_client = CoinGeckoAPI()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, 'to use this bot, send it crypto name, like bitcoin')


# print(coin_client.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd'])

@bot.message_handler()
def crypto_price_message_handler(message):
    crypto_id = message.text
    price_response = coin_client.get_price(ids=crypto_id, vs_currencies='usd')
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    if price_response:
        price = price_response[crypto_id]['usd']
        bot.send_message(chat_id=message.chat.id, text=f"{date_time} - Price of {crypto_id}: {price}")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Price of {crypto_id} was not found")


if __name__ == '__main__':
    bot.polling()
