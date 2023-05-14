from fable.credentials import bot_token
from fable.ocr.char_rec import character_recognise
from fable.summarizer.summarizer import summarize

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from PIL import Image
import io


introduction = 'Welcome to interaction with F.A.B.L.E, please read the description and feel free to ask the bot a question!'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=introduction)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    summarized_text = summarize(text)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summarized_text)

async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img_file = await context.bot.get_file(update.message.document)
    
    image_bytes = io.BytesIO()
    
    await img_file.download_to_memory(out=image_bytes)
    
    image_bytes.seek(0)
    
    img = Image.open(image_bytes).convert('L')
    
    text = character_recognise(img)
    
    summarized_text = summarize(text)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summarized_text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT, message)
    image_handler = MessageHandler(filters.Document.IMAGE, image)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    application.add_handler(image_handler)
    
    application.run_polling()
