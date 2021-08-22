from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.operations import delete, increment, decrement, add, subtract

db = TinyDB("user_db.json")

User = Query()

chat_id = 1827

# db.truncate()

def add_user (chat_id):
    db.insert({
        "user_id": chat_id,
        "likes":0,
        "dislikes":0,
        "messages":0,
        "user_name": "Otabek"
    })

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


add_user(chat_id)  
add_like(chat_id)
add_dislike(chat_id)
add_message(chat_id)

# db.remove()
# insert()
# for i in db:
#     print(i)

print(db.search(User.user_id == chat_id)[0]["likes"])