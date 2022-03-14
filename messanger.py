from initializations import bot
from messages import MESSAGES
from comands import COMMANDS
from addons.owm import ReturnWeather

def message_handler(chat_id, text, name):
    if text == '/start':
        bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
    if text[0] == '/':
        if text == '/sub':
            bot.add_u(chat_id)
        elif text == '/unsub':
            bot.remove_u(chat_id)
        elif text == '/weather':
            bot.send_message(chat_id, COMMANDS[text], state=1)
    else:
        bot.send_message(chat_id, text[::-1])

def first_state(chat_id, text):
    answer = ReturnWeather(text)
    if answer == "Вы ошиблись в названии города, попробуйте еще раз":
        bot.send_message(chat_id, answer, state=1)
    else:
        bot.send_message(chat_id, answer)

def creating_message(chat_id, state):
    bot.send_message(chat_id, MESSAGES[state])
