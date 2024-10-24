from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command function
def start(update, context):
    update.message.reply_text('Hi! I am a simple bot. Ask me math questions or simple general queries.')

# Define a function to handle math calculations
def handle_math(update, context):
    try:
        # Evaluate the user's message as a math expression
        user_input = update.message.text
        result = eval(user_input)
        update.message.reply_text(f"The result is: {result}")
    except Exception as e:
        update.message.reply_text(f"Sorry, I couldn't compute that. Error: {e}")

# Define a function to handle simple text responses
def handle_text(update, context):
    text = update.message.text.lower()
    if "hello" in text or "hi" in text:
        update.message.reply_text('Hello! How can I assist you today?')
    elif "your name" in text:
        update.message.reply_text("I'm a simple bot created to answer math and basic queries!")
    else:
        update.message.reply_text("I am not sure about that. You can try asking me a math question.")

# Error handler function
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Replace TOKEN with your bot token from BotFather
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Add a handler for math expressions
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_math))

    # Add a handler for general text queries
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT
    updater.idle()

if __name__ == '__main__':
    main()
