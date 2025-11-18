from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

ADMIN_IDS = [123456789]  # später ersetzen

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return await update.message.reply_text("⛔ Keine Berechtigung.")

    await update.message.reply_text("👑 Admin-Panel kommt später rein.")

def get_admin_handler():
    return CommandHandler("admin", admin)
