import json
from json.decoder import JSONDecodeError

def add_likes(chat_id, like, dislike):
    pass
def add_newuser_likes(chat_id, like, dislike):
    pass


dict1 = {}
try:
    dict1 = json.load(open("data_file.json"))
    # dict1 = {}
    print(dict1)
except JSONDecodeError:
    dict1 = {}
    pass

likes = 1
dislikes =1
chat_id =1
for i in range(11,15):
    if dict1.get(str(chat_id+i)) is not None:
        dict1[str(chat_id+i)] = {"likes": likes, "dislikes": dislikes}
    else:
        dict1[str(chat_id+i)] = {"likes": 0, "dislikes": 0}

y =json.dumps(dict1)
f =open("data_file.json", "w")
print("Done writing")
f.write(y)
f.close()

a = {11111111:{"likes": likes+i, "dislikes": dislikes+i}}



