import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.getenv('TOKEN')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Send me a message, and I'll detect if it's spam.")


async def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    response = requests.post(TELEGRAM_API_URL, json={"text": user_text})

    if response.status_code == 200:
        result = response.json()
        await update.message.reply_text(f"Prediction: {result['label']} (Score: {result['score']:.2f})")
    else:
        await update.message.reply_text("Error processing your request.")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
