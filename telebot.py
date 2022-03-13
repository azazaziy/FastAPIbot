#!/usr/bin/env python3
import requests



class Bot:

    def __init__(self, TOKEN, DATABASE):
        self.url = f'https://api.telegram.org/bot{TOKEN}/'
        self.database = DATABASE
        self.webhook = f'{self.url}setWebhook?url=https://4db03e18e5bad0.lhrtunnel.link'

    def get_updates(self):
        r = requests.get(self.url + 'getUpdates')
        return r.json()

    def send_message(self, chat_id, text='simple_text'):
        message = {'chat_id': chat_id, 'text': text}
        url = self.url + 'sendMessage'
        response = requests.post(url, json=message)
        return response.json()

    def add_sub(self, chat_id):
        self.database.add_subscriber(chat_id)

    def remove_sub(self, chat_id):
        self.database.remove_subscriber(chat_id)

# curl -X "POST" "https://api.telegram.org/bot1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg/setWebhook" -d '{"url": "https://36f10ccf8c4b91.lhrtunnel.link"}' -H 'Content-Type: application/json; charset=utf-8'
