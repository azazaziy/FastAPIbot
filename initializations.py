from postgresser import Postgresser
from telebot import Bot

from config import DB_URI
from config import TOKEN
from config import WEBHOOK

bot = Bot(TOKEN, WEBHOOK)
db = Postgresser(DB_URI)
