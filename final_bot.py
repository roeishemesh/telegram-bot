from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import telegram
import stock_or_crypto as choose

user_id = "index_bot"
bot = telegram.Bot(token="1598974200:AAGZdylImna2HeEiJ7929OQqo3uC3dJ0qF8")


def start(update, context):
    bot_welcome = """
    Hii!
    Welcome to stock exchange telegram bot!
    You can write an index, a stock, a stock symbol or a cryptocurrency name,
    and you will receive her value and her daily change.
    If you are looking for cryptocurrency - 
    write "crypto" after the cryptocurrency name or symbol
    For example - "BTC crypto".
    All the information is belonging to the website www.investing.com"""
    context.bot.send_message(chat_id=update.message.chat_id, text=bot_welcome)


def getinfo(update):
    update.message.reply_text(choose.stock_or_crypto(update.message.text))


updater = Updater(token="1598974200:AAGZdylImna2HeEiJ7929OQqo3uC3dJ0qF8", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, getinfo))
updater.start_polling()
updater.idle()
