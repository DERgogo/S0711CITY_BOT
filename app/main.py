from telegram.ext import ApplicationBuilder
from app.config import BOT_TOKEN, WEBHOOK_URL
from app.handlers.start_handler import get_start_handler


async def set_webhook(app):
    # Webhook setzen
    await app.bot.set_webhook(url=WEBHOOK_URL)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler laden
    app.add_handler(get_start_handler())

    # Webhook aktivieren
    app.post_init = set_webhook

    # Bot starten (Webhook-Modus)
    app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        url_path=""
    )


if __name__ == "__main__":
    main()
