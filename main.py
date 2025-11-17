from fastapi import FastAPI, Request
from app.core.bot_init import bot, application
from app.core.webhook import set_webhook

app = FastAPI()

@app.on_event("startup")
async def startup():
    await set_webhook()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await application.update_queue.put(update)
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"status": "Future0711Y online"}
