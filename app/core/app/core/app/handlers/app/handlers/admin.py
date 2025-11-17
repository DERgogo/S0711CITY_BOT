from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

ADMINS = [123456789]

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return
    await update.message.reply_text("Admin Panel aktiv.")

admin_handler = CommandHandler("admin", admin)
