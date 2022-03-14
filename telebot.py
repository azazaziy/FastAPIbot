import requests


class Bot:

    def __init__(self, TOKEN, WEBHOOK):
        self.url = f'https://api.telegram.org/bot{TOKEN}/'
        self.webhook = f'{self.url}setWebhook?url={WEBHOOK}/bot'
        self.API_URL = WEBHOOK

    def send_message(self, chat_id, text='simple_text'):
        message = {'chat_id': chat_id, 'text': text}
        url = self.url + 'sendMessage'
        response = requests.post(url, json=message)
        return response.json()

    def add_u(self, user_id):
        requests.get(f'{self.API_URL}/add_user?user_id={user_id}')

    def remove_u(self, user_id):
        requests.get(f'{self.API_URL}/remove_user?user_id={user_id}')

