from messages import MESSAGES
from comands import COMMANDS
from initializations import bot



def message_handler(chat_id, text, name):
    if text[0] == '/':
        if text == '/sub':
            check = bot.add_u(chat_id)
            if check == 'success':
                bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
            elif check == 'existed_user':
                bot.send_message(chat_id, MESSAGES['existed_user'])
        elif text == '/unsub':
            bot.remove_u(chat_id)

    else:
        bot.send_message(chat_id, text[::-1])
