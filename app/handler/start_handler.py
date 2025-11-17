from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    greeting = (
        f"👋 Yo {user.first_name}, willkommen im *S0711CITY BOT*!\n\n"
        "🌆 Stuttgart-Vibes\n"
        "⚙️ Trap-Tools\n"
        "🧩 Menüs\n\n"
        "Tippe /menu für die Optionen."
    )

    await update.message.reply_text(greeting, parse_mode="Markdown")


def get_start_handler():
    return CommandHandler("start", start)
