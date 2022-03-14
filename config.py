#HEROCU
import os

DB_URI = os.environ.get('DB_URI')
TOKEN = os.environ.get('TOKEN')
WEBHOOK = os.environ.get('WEBHOOK')

#LOCALHOST
# DB_URI = 'postgres://hpuuhumbzapiwo:47e8f7d2dd53f6dd86c58288f824433b9b602e18654b990840cedd2fae8cc073@ec2-54-194-147-61.eu-west-1.compute.amazonaws.com:5432/d68ekbl5kl6910'
# TOKEN = '1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg'
# WEBHOOK = 'https://19b201caf3a964.lhrtunnel.link'

#https://api.telegram.org/bot1139412331:AAHH5phrKI8YLOtKPYm9VcwIpZUL23PpWIg/setWebhook?url=https://19b201caf3a964.lhrtunnel.link/bot