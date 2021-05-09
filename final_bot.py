from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import telegram
import stock_or_crypto as choose

user_id = "index_bot"
bot = telegram.Bot(token="1598974200:AAGZdylImna2HeEiJ7929OQqo3uC3dJ0qF8")


def start(update, context):
    bot_welcome = """
    Hii!
    welcome to stock telegram bot!
    you can give index name, stock name or stock symbol.
    i will give you the stock price
    and if it go up or down today.
    if you lock for crypto coin:
    please write "crypto" after
    your crypto name (BTC crypto).
    all the information is from
    investing.com """
    context.bot.send_message(chat_id=update.message.chat_id, text=bot_welcome)


def getinfo(update, context):
    update.message.reply_text(choose.stock_or_crypto(update.message.text))


updater = Updater(token="1598974200:AAGZdylImna2HeEiJ7929OQqo3uC3dJ0qF8", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, getinfo))
updater.start_polling()
updater.idle()
