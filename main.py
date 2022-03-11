from fastapi import FastAPI
from fastapi import Query
from schemas import Message
from telebot import Bot
from sqliter import SQLighter

app = FastAPI()
db = SQLighter('db.db')
bot = Bot(TOKEN='1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg',
          WEBHOOK='',
          DATABASE=db)

@app.get('/')
async def home():
    return {'key':'Hello'}

@app.get('/add_user')
async def get_item( q:str = Query(None, min_length=8, max_length=10)):
    return {'q':q}

@app.post('/send_mesage')
def send_message(message: Message):
    return message

