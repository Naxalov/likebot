import json
from json.decoder import JSONDecodeError


def db_update (chat_id, likes, dislikes):
    dict1 = {}
    try:
        dict1 = json.load(open("data_file.json"))

        print(dict1)
    except JSONDecodeError:
        dict1 = {}
        pass

 
    if dict1.get(str(chat_id)) is not None:
        dict1[str(chat_id)] = {"likes": likes, "dislikes": dislikes}
        print("Yangi ID")
    else:
        dict1[str(chat_id)] = {"likes": dict1[chat_id][likes] + 1, "dislikes": dict1[chat_id][likes] + 1}
        print("Mavjud Id update")
    y =json.dumps(dict1)
    f =open("data_file.json", "w")
    
    f.write(y)
    f.close()

db_update(10, 5,7)
