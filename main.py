
from telegram import bot
from telegram.ext import Updater,MessageHandler,Filters,CommandHandler
import telegram

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram.keyboardbutton import KeyboardButton

TOKEN = "1920162914:AAEVHgICKGUttXJzooTQ_d-w05LFLEhrD_M"

like = 0
dislike = 0

def start(update, context):
    bot =context.bot
    update.message.reply_html(
        f'<b>Assalomu alaykum, {update.message.from_user.first_name}</b>\n \nMen likelarni sanaydigan botmnan')
    return 1

def like_count(update, context):
    global like
    global dislike
    bot = context.bot
    user_text = update.message.text
    chat_id = update.message.chat.id
    
    if user_text == "👍":
        like += 1
    elif user_text == "👎":
        dislike += 1
    text = f"Like: {like} \nDislike: {dislike}" 
    bot.send_message(chat_id, text)
    print(chat_id)

def user_data (chat_id, like, dislike):
    file1 = open("data_file.json", r)


def echo(update,context):
    pass

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, like_count))
# updater.dispatcher.add_handler(MessageHandler(Filters.location, callback=location_user))

updater.start_polling()
updater.idle()
