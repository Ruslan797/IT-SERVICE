from fastapi import FastAPI
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# Загружаем переменные из .env
load_dotenv()

TELEGRAM_BOT = os.getenv("TELEGRAM_BOT")

if TELEGRAM_BOT:
    print("Telegram token loaded successfully")
else:
    print("Telegram token NOT found")


# FastAPI
app = FastAPI()


@app.get("/")
def home():
    return {"message": "IT Service is running"}


# Telegram Bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hallo! 👋\n"
        "Willkommen beim IT-Service Hamburg & Norderstedt.\n\n"
        "Wie kann ich Ihnen helfen?"
    )


def run_bot():
    telegram_app = Application.builder().token(TELEGRAM_BOT).build()

    telegram_app.add_handler(
        CommandHandler("start", start)
    )

    print("Telegram bot is running...")

    telegram_app.run_polling()


if __name__ == "__main__":
    run_bot()