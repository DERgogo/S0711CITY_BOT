from config import APP_URL, BOT_TOKEN, WEBHOOK_URL
import httpx

async def set_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"url": WEBHOOK_URL})
