from telegram.ext import CommandHandler, ContextTypes
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("AI Chat", callback_data="ai")],
        [InlineKeyboardButton("YouTube Feed", callback_data="yt")],
        [InlineKeyboardButton("Shop", callback_data="shop")]
    ]
    await update.message.reply_text("Future0711Y Menü:", reply_markup=InlineKeyboardMarkup(kb))

menu_handler = CommandHandler("menu", menu)
