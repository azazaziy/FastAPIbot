import requests
from postgresser import Postgresser

db = Postgresser('postgres://vazkibwucrvyqe:3992c06da77a8456a1916565b80839b38c43ce7924d84a9327d8caa0fb12f7e8@ec2-176-34-105-15.eu-west-1.compute.amazonaws.com:5432/d6lc9s12vi2h2o')



class Bot:

    def __init__(self, TOKEN):
        self.url = f'https://api.telegram.org/bot{TOKEN}/'
        self.webhook = f'{self.url}setWebhook?url=https://telegramwebhookapi.herokuapp.com/bot'


    def send_message(self, chat_id, text='simple_text'):
        message = {'chat_id': chat_id, 'text': text}
        url = self.url + 'sendMessage'
        response = requests.post(url, json=message)
        return response.json()

    def add_u(self, chat_id):
        return db.add_user(chat_id)

    def remove_u(self, chat_id):
        db.remove_user(chat_id)

    def return_users_id(self):
        temp = db.return_users()
        return [x for t in temp for x in t]
