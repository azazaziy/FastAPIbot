from messages import MESSAGES
from comands import COMMANDS
from initializations import bot



def message_handler(chat_id, text, name):
    print('handler catch:\t', text)
    if text[0] == '/':
        print('bot recognize command')
        if text == '/sub':
            print('subscribe command')
            bot.add_u(chat_id)
        #
        #     if check == 'success adding':
        #         bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
        #     elif check == 'existed user':
        #         bot.send_message(chat_id, MESSAGES['existed_user'])
        elif text == '/unsub':
            check = bot.remove_u(chat_id)
            print(check)
        #     if check == 'success remove':
        #         bot.send_message(chat_id, COMMANDS[text].format(NAME=name))
        #     elif check == 'not existed user':
        #         bot.send_message(chat_id, MESSAGES['not exited user'])
        #     print('unsubscribe command')


    else:
        print('simple text')
        bot.send_message(chat_id, text[::-1])
