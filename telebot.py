import requests


class Bot:

    def __init__(self, TOKEN, WEBHOOK, DATABASE):
        self.url = f'https://api.telegram.org/bot{TOKEN}/'
        self.webhook = f'{self.url}setWebhook?url={WEBHOOK}'
        self.database = DATABASE

    def send_message(self, chat_id, text='simple_text'):
        message = {'chat_id': chat_id, 'text': text}
        url = self.url + 'sendMessage'
        response = requests.post(url, json=message)
        return response.json()

    def add_sub(self, chat_id):
        self.database.add_subscriber(chat_id)

    def remove_sub(self, chat_id):
        self.database.remove_subscriber(chat_id)


