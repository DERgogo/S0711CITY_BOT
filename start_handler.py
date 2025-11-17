from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"🔥 Willkommen {user.first_name}!\n"
        f"City-Lights ON – dein S0711CITYBOT läuft.\n\n"
        f"Wähle eine Option:"
    )

    keyboard = [
        [InlineKeyboardButton("🚦 Hauptmenü", callback_data="main_menu")],
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = "📍 Hauptmenü\nWas brauchst du?"

    keyboard = [
        [InlineKeyboardButton("ℹ Info", callback_data="info")],
        [InlineKeyboardButton("💬 Support", callback_data="support")],
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def info_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("ℹ Infos… (kommt später mehr)")

async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("💬 Support… (kommt später mehr)")
