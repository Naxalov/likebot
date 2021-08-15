# def user_likes (chat_id, user_text):
#     like =0
#     dislike =0
#     user_like = {}
#     if user_text == "a":
#         like +=1
#         user_like = ["chat_id"]["likes"] = like
#     elif user_text == "b":
#         dislike +=1
#         user_like = ["chat_id"]["dislikes"] = dislike
#     print(user_like)

# user_likes(123, "a")


import json


user_likes ={}
def user_get_likes(chat_id, user_text):
    global user_likes
    user_likes ={}
    if user_likes.get(chat_id, "no") == "no":
        likes = 0
        dislikes = 0
        if user_text == "a":
            likes +=1
            user_likes.update({chat_id: {"likes": likes}})
            print(user_likes)
        elif user_text == "b":
            dislikes +=1
            user_likes.update({chat_id: {"dislikes": dislikes}})
        print(user_likes)
            
    else:
        likes = user_likes[chat_id]["likes"]
        dislikes = user_likes[chat_id]["dislikes"]
        if user_text == "a":
            likes +=1
            user_likes.update({chat_id: {"likes": likes, "dislikes": dislikes}})
            print(user_likes)
        elif user_text == "b":
            dislikes +=1
            user_likes.update({chat_id: {"likes": likes, "dislikes": dislikes}})

        print(user_likes)

user_get_likes(112, "a")

def check_user_id (chat_id):
    pass

def file_read (file_name):
    pass

def file_append (user_likes):
    pass


