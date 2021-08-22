from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.operations import delete, increment, decrement, add, subtract

db = TinyDB("user_db.json")

User = Query()

chat_id = 1827

# db.truncate()

def add_user(db_user,chat):
    # db.insert({
    #     "user_id": chat_id,
    #     "likes":0,
    #     "dislikes":0,
    #     "messages":0,
    #     "user_name": "Otabek"
    # })
    chat_id = chat.id
    username = chat.username
    username = chat.username
    first_name= chat.first_name
    last_name= chat.last_name
    bio = chat.bio
    # User document
    user = {
        'chat_id':chat_id,
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
        'bio':bio
    }
    db_user.insert(user)    
    print(chat_id,username)

def add_like(chat_id):
    db.update(increment("likes"), User.user_id == chat_id)
def add_dislike (chat_id):
    db.update(increment("dislikes"), User.user_id == chat_id)
def add_message(chat_id):
    db.update(increment("messages"), User.user_id == chat_id)

def get_user_data (chat_id):
    likes = db.search(User.user_id == chat_id)[0]["likes"]
    dislikes = db.search(User.user_id == chat_id)[0]["dislikes"]
    messages = db.search(User.user_id == chat_id)[0]["messages"]


# add_user(chat_id)  
# add_like(chat_id)
# add_dislike(chat_id)
# add_message(chat_id)

# db.remove()
# insert()
# for i in db:
#     print(i)

# print(db.search(User.user_id == chat_id)[0]["likes"])