
import json
from os import write
from telegram import bot
from telegram.ext import Updater,MessageHandler,Filters,CommandHandler


from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram.keyboardbutton import KeyboardButton
from tinydb import TinyDB
TOKEN = "1920162914:AAEVHgICKGUttXJzooTQ_d-w05LFLEhrD_M"
db = TinyDB('user.json')

def start(update, context):
    bot =context.bot
    # GET user information
    chat_id = update.message.chat.id
    username = update.message.chat.username
    first_name= update.message.chat.first_name
    last_name= update.message.chat.last_name
    bio = update.message.chat.bio
    #User document
    user = {
        'chat_id':chat_id,
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
        'bio':bio
    }
    update.message.reply_html(
        f'<b>Assalomu alaykum, {update.message.from_user.first_name}</b>\n \nMen likelarni sanaydigan botmnan. \n\nIshlatish uchun Like yoki Dislike smayliklarini yuboring')
    
    db.insert(user)    

    return 1

def like_count(update, context):

    db_like_file =open("data_file.json", "r")
    db_like =json.loads(db_like_file.read())
    print(db_like)
    db_like_file.close()
    bot = context.bot
    user_text = update.message.text
    chat_id = update.message.chat.id
    db_like.setdefault(str(chat_id),{
        "likes":0,
        "dislikes":0,
        "messages":0,
        "user_name": update.message.from_user.first_name
    })
    print(db_like)
    if user_text == "👍":
        db_like[str(chat_id)]['likes']+=1
    elif user_text == "👎":
        db_like[str(chat_id)]['dislikes']+=1
    else:
        db_like[str(chat_id)]['messages']+=1
    text = f"\nIsm:{update.message.from_user.first_name}\n\nLikelar soni 👍: {db_like[str(chat_id)]['likes']} \nDislikelar soni 👎: {db_like[str(chat_id)]['dislikes']} \nXabarlar soni: {db_like[str(chat_id)]['messages']}" 
    bot.send_message(chat_id, text)
    db_like_file =open("data_file.json", "w")

    db_like_file.write(json.dumps(db_like))

    db_like_file.close()
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
