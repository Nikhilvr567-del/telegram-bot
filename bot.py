from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

TOKEN = os.environ.get("BOT_TOKEN")

async def delete_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text
        
        if text and (
            "teleprotectorbot" in text.lower() or
            "reports are blocked" in text.lower() or
            "channels are saved" in text.lower()
        ):
            try:
                await context.bot.delete_message(
                    chat_id=update.channel_post.chat_id,
                    message_id=update.channel_post.message_id
                )
            except Exception as e:
                print(e)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, delete_messages))

app.run_polling()
