from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder

from app.config import BOT_TOKEN

telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
fastapi_app = FastAPI()


@fastapi_app.on_event("startup")
async def startup_event():
    # Telegram App muss initialisiert werden
    await telegram_app.initialize()


@fastapi_app.post("/")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}
