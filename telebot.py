import requests
from postgresser import Postgresser


class Bot:

    def __init__(self, TOKEN, WEBHOOK):
        self.url = f'https://api.telegram.org/bot{TOKEN}/'
        self.webhook = f'{self.url}setWebhook?url={WEBHOOK}'

    def send_message(self, chat_id, text='simple_text'):
        message = {'chat_id': chat_id, 'text': text}
        url = self.url + 'sendMessage'
        response = requests.post(url, json=message)
        return response.json()

    def add_u(self, chat_id):
        requests.get()

    def remove_u(self, chat_id):
        db.remove_user(chat_id)

    def return_users_id(self):
        temp = db.return_users()
        return [x for t in temp for x in t]
