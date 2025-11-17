from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from app.utils.texts import get_welcome_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = get_welcome_message()
    await update.message.reply_text(msg)

start_handler = CommandHandler("start", start)
