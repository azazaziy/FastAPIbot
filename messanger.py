from messages import MESSAGES
from comands import COMMANDS
import json

from qwerty import bot




def write_json(data, file_name='answer.json'):  # ЗАПИСЬ JSON
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def running(chat_id, text, name):
    if text[0] == '/':
        bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
    else:
        bot.send_message(chat_id, text[::-1])
