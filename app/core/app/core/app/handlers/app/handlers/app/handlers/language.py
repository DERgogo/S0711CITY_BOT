from telegram.ext import CommandHandler
from telegram import Update
from app.utils.texts import set_language

async def language(update: Update, context):
    lang = context.args[0] if context.args else "de"
    set_language(lang)
    await update.message.reply_text(f"Sprache geändert: {lang.upper()}")

language_handler = CommandHandler("lang", language)
