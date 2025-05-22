# config.py

# Stocks and crypto symbols to track
STOCK_SYMBOLS = ["AAPL", "MSFT", "TSLA"]
CRYPTO_SYMBOLS = ["bitcoin", "ethereum", "dogecoin"]  # Use CoinGecko IDs

# API Keys
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
COINGECKO_API_BASE = "https://api.coingecko.com/api/v3"

# Telegram bot config
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_telegram_chat_id"

# Signal thresholds
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70

# Other config
DATA_FETCH_INTERVAL = "daily"  # 'daily' or 'weekly'
