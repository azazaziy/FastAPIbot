from fastapi import FastAPI
from fastapi import Query
from fastapi import Request

import json

from messanger import message_handler
from messanger import creating_message
from initializations import db
from initializations import bot

app = FastAPI()


@app.get('/')
async def home():
    return {'ОГО': 'ОНО РАБОТАЕТ'}


@app.post('/bot')
async def bot_polling(request: Request):
    response = await request.body()
    response = response.decode('utf-8')
    json_responce = json.loads(response)
    try:
        chat_id = json_responce['message']['chat']['id']
        text = json_responce['message']['text']
        name = json_responce['message']['chat']['first_name'] + ' ' + json_responce['message']['chat']['last_name']
        text_message = True
    except:
        text_message = False
    if text_message:
        message_handler(chat_id, text, name)
    return {"received_request_body": json_responce}


@app.get('/add_user')
async def add_u(user_id: str = Query(None, min_length=8, max_length=10)):
    result = db.add_user(user_id)
    creating_message(user_id, result)
    return {'user added': f'user id:\t{user_id}'}


@app.get('/remove_user')
async def re_u(user_id: str = Query(None, min_length=8, max_length=10)):
    result = db.remove_user(user_id)
    creating_message(user_id, result)
    return {'user removed': f'user id:\t{user_id}'}


@app.get('/send_message')
async def send_message(message: str = Query(None, min_length=1)):
    users = db.return_users()
    for i in users:
        bot.send_message(i, message)
    return {'send message': users}
