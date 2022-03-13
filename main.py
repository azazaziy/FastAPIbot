from fastapi import FastAPI
from fastapi import Query
from fastapi import Request

from messanger import bot
from messanger import db
from messanger import write_json
from messanger import running
import json
#heroku url
#https://git.heroku.com/telegramwebhookapi.git
app = FastAPI()

@app.post('/')
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
async def add_user(user_id: str = Query(None, min_length=8, max_length=10)):
    await bot.add_sub(user_id)
    return {'q': user_id}

@app.get('/remove_subscriber')
async def re_user(user_id: str = Query(None, min_length=8, max_length=10)):
    await bot.remove_sub(user_id)
    return {'q': user_id}


@app.get('/send_mesage')
async def send_message(message: str = Query(None, min_length=1)):
    users = [x for t in db .return_users() for x in t]
    for i in users:
        bot.send_message(i, message)
    return {'send message'}
