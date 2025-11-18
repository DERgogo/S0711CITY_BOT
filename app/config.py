import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL")  # z.B. https://ravishing-learning.up.railway.app

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = APP_URL + WEBHOOK_PATH
