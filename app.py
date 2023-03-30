from fable.credentials import bot_token, bot_username

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

introduction = 'Welcome to interaction with F.A.B.L.E, please read the description and feel free to ask the bot a question!'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=introduction)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am currently in production, please check back later.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    application.run_polling()