from fastapi import FastAPI, Request
from app.config import WEBHOOK_PATH
from app.bot import create_bot

telegram_app = create_bot()
fastapi_app = FastAPI()

@fastapi_app.get("/healthz")
async def health():
    return {"status": "ok"}

@fastapi_app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    update = await request.json()
    await telegram_app.update_queue.put(update)
    return {"ok": True}
