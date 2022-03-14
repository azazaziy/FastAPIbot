from initializations import bot
from messages import MESSAGES
from comands import COMMANDS


def message_handler(chat_id, text, name):
    if text[0] == '/':
        if text == '/sub':
            bot.add_u(chat_id)
        elif text == '/unsub':
            bot.remove_u(chat_id)
        elif text == '/start':
            bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
    else:
        bot.send_message(chat_id, text[::-1])


def creating_message(chat_id, state):
    bot.send_message(chat_id, MESSAGES[state])
