import os

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)


load_dotenv()

TELEGRAM_BOT = os.getenv("TELEGRAM_BOT")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

TELEGRAM_CHAT_ID = int(telegram_chat_id) if telegram_chat_id else None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("CHAT ID:", update.effective_chat.id)

    keyboard = [
        [
            InlineKeyboardButton(
                "PC & Laptop",
                callback_data="pc_laptop",
            )
        ],
        [
            InlineKeyboardButton(
                "Windows",
                callback_data="windows",
            )
        ],
        [
            InlineKeyboardButton(
                "Linux",
                callback_data="linux",
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hallo!\n"
        "Willkommen beim IT-Service Hamburg & Norderstedt.\n\n"
        "Wie kann ich Ihnen helfen?",
        reply_markup=reply_markup,
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    if TELEGRAM_CHAT_ID:
        await context.bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text="Neue Anfrage beim IT-Service",
        )

    if query.data == "windows":
        await query.message.reply_text(
            "Beschreiben Sie bitte Ihr Windows-Problem."
        )


def run_bot():
    if not TELEGRAM_BOT:
        print("Telegram bot token not found.")
        return

    telegram_app = Application.builder().token(TELEGRAM_BOT).build()

    telegram_app.add_handler(
        CommandHandler("start", start)
    )

    telegram_app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Telegram bot is running...")
    telegram_app.run_polling()


if __name__ == "__main__":
    run_bot()