
import json
from os import write
from telegram import bot
from telegram.ext import Updater,MessageHandler,Filters,CommandHandler


from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram.keyboardbutton import KeyboardButton
from tinydb import TinyDB
from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.operations import delete, increment

from db_test import add_user


TOKEN = "1920162914:AAEVHgICKGUttXJzooTQ_d-w05LFLEhrD_M"

db_user = TinyDB("user_db.json")
db = TinyDB("like_db.json")

User = Query()

def start(update, context):
    bot =context.bot
    # GET user information
    chat = update.message.chat
    add_user(db_user,chat)

    update.message.reply_html(
        f'<b>Assalomu alaykum, {update.message.from_user.first_name}</b>\n \nMen likelarni sanaydigan botmnan. \n\nIshlatish uchun Like yoki Dislike smayliklarini yuboring')
    

    return 1

def like_count(update, context):
    bot = context.bot
    user_text = update.message.text
    User = Query()
    chat_id = update.message.chat.id

   
    db.insert({
        "user_id": chat_id,
        "likes":0,
        "dislikes":0,
        "messages":0,
        "user_name": update.message.from_user.first_name
    })

    likes = db.search(User.user_id == chat_id)[0]["likes"]
    dislikes = db.search(User.user_id == chat_id)[0]["dislikes"]
    messages = db.search(User.user_id == chat_id)[0]["messages"]
    print(db.all)
    if user_text == "👍":
        db.update(increment("likes"), User.user_id == chat_id)
    elif user_text == "👎":
        db.update(increment("dislikes"), User.user_id == chat_id)
    else:
        db.update(increment("messages"), User.user_id == chat_id)

    text = f"\nIsm:{update.message.from_user.first_name}\n\nLikelar soni 👍: {likes}\nDislikelar soni 👎:{dislikes} \nXabarlar soni: {messages}" 
    bot.send_message(chat_id, text)
  
    print(chat_id)




def echo(update,context):
    pass

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, like_count))
# updater.dispatcher.add_handler(MessageHandler(Filters.location, callback=location_user))

updater.start_polling()
updater.idle()
