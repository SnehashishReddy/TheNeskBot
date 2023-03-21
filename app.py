import os
import sys
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
import logging
from burrybot.credentials import bot_token, bot_user_name, webhook_url


"""
Boilerplate code to add parent directory to Python PATH
"""
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


"""
The below code is executed when the bot is started
It is responsible for:
-> Recieving text
-> Determining the intent of the text
-> Calling the appropriate module based on the intent
-> Sending a response back to the user
"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Create an Updater object and pass in your bot's token
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


# Set the bot's username and webhook URL
updater.bot.username = bot_user_name
updater.bot.setWebhook(webhook_url)


# Define a function to handle incoming messages
def handle_message(update: Update, context):
    # Get the message text from the user
    message_text = update.message.text
    
    # Determine the intent of the message using a separate function
    intent = determine_intent(message_text)
    
    # Call the appropriate module based on the intent and get a response
    response = call_module(intent)
    
    # Send the response back to the user
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


# Define a function to determine the intent of a message
def determine_intent(message_text):
    # Placeholder logic to determine intent
    return 'intent'


# Define a function to call the appropriate module based on intent
def call_module(intent):
    # Placeholder logic to call module
    return 'response'


# Set up a message handler to handle incoming messages
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)


# Start the bot using webhook
updater.start_webhook(listen='0.0.0.0', port=int(os.environ.get('PORT', '8443')), url_path=bot_token)
updater.bot.setWebhook(webhook_url)
