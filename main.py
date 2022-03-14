from fastapi import FastAPI
from fastapi import Query
from fastapi import Request

from messanger import write_json
from messanger import running
import json

from postgresser import Postgresser
from telebot import Bot


db = Postgresser('postgres://vazkibwucrvyqe:3992c06da77a8456a1916565b80839b38c43ce7924d84a9327d8caa0fb12f7e8@ec2-176-34-105-15.eu-west-1.compute.amazonaws.com:5432/d6lc9s12vi2h2o')
bot = Bot(TOKEN='1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg')



app = FastAPI()
@app.get('/')
async def home():
    return {'q': 'qwer'}

@app.post('/bot')
async def bot_polling(request: Request):
    responce = await request.body()
    responce = responce.decode('utf-8')
    json_responce = json.loads(responce)
    write_json(json_responce)
    try:
        chat_id = json_responce['message']['chat']['id']
        text = json_responce['message']['text']
        name = json_responce['message']['chat']['first_name'] + ' ' + json_responce['message']['chat']['last_name']
        text_message = True
    except:
        text_message = False
    if text_message:
        running(chat_id, text, name)
    # elif command:
    #     comand(chat_id, text, name)
    return {"received_request_body": json_responce}

@app.get('/add_user')
async def add_u(user_id: str = Query(None, min_length=8, max_length=10)):
    db.add_user(user_id)
    return {'q': user_id}

@app.get('/remove_user')
async def re_u(user_id: str = Query(None, min_length=8, max_length=10)):
    db.remove_user(user_id)
    return {'q': user_id}


@app.get('/send_mesage')
async def send_message(message: str = Query(None, min_length=1)):
    users = bot.return_users_id()
    for i in users:
        bot.send_message(i, message)
    return {'send message': users}
