import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Welcome to Owner Swifty!\n'
        'Use /price [coin] to get current price\n'
        'Example: /price bitcoin'
    )

def get_price(update: Update, context: CallbackContext):
    """
    Fetch and display the current price of a cryptocurrency in USD.
    This function makes a request to the CoinGecko API to get the current price
    of a specified cryptocurrency and sends it back as a message through the Telegram bot.
    Args:
        update (Update): The update object from Telegram containing message information
        context (CallbackContext): The context object for accessing arguments and bot data
    Returns:
        None: The function sends a message through the bot instead of returning values
    Raises:
        Exception: Catches any errors during API request or data processing and sends an error message
    Example:
        To get Bitcoin price:
        /price bitcoin
    Note:
        The coin name should match CoinGecko's API identifier format
    """
    try:
        coin = context.args[0].lower()
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd')
        data = response.json()
        
        if coin in data and 'usd' in data[coin]:
            price = data[coin]['usd']
            update.message.reply_text(f'Current {coin.upper()} price: ${price:,.2f}')
        else:
            update.message.reply_text('Coin not found. Try /price bitcoin')

    except Exception as e:
        update.message.reply_text('Error fetching price. Please try again.')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", get_price))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()