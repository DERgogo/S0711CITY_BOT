from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📍 *S0711CITY MENU*\n\n"
        "1️⃣ Info\n"
        "2️⃣ Projekte\n"
        "3️⃣ Kontakt\n\n"
        "Mehr Features kommen… 🔧"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

def get_menu_handler():
    return CommandHandler("menu", menu)
