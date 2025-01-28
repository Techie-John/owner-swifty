# owner-swifty
A Telegram bot that fetches cryptocurrency prices using the CoinGecko API.

## Features
- Get current prices for any cryptocurrency supported by CoinGecko
- Simple command interface
- Real-time price updates

## Setup
1. Install dependencies:
```bash
pip install python-telegram-bot requests
```

2. Set environment variable:
```bash
export TELEGRAM_BOT_TOKEN='your_token_here'
```

## Usage
- `/start` - Display welcome message and instructions
- `/price [coin]` - Get current price of specified cryptocurrency
    - Example: `/price bitcoin`

## Dependencies
- python-telegram-bot
- requests

## Error Handling
- Handles invalid coin names
- Graceful error handling for API failures