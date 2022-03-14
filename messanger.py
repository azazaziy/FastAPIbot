from telebot import Bot
from messages import MESSAGES
from comands import COMMANDS

import json
from postgresser import Postgresser


db = Postgresser('postgres://vazkibwucrvyqe:3992c06da77a8456a1916565b80839b38c43ce7924d84a9327d8caa0fb12f7e8@ec2-176-34-105-15.eu-west-1.compute.amazonaws.com:5432/d6lc9s12vi2h2o')
bot = Bot(TOKEN='1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg',
          DATABASE=db)


def write_json(data, file_name='answer.json'):  # ЗАПИСЬ JSON
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def running(chat_id, text, name):
    if text[0] == '/':
        bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
    else:
        bot.send_message(chat_id, text[::-1])
