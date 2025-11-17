from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

application = ApplicationBuilder().token(BOT_TOKEN).build()
bot = application.bot
