from telegram.ext import ApplicationBuilder
from app.config import BOT_TOKEN
from app.handlers.start_handler import get_start_handler

def create_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(get_start_handler())
    return app
