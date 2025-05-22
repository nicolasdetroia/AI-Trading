# run_signals.py
from data_fetcher import fetch_stock_data, fetch_crypto_data
from indicators import add_indicators
from signal_generator import generate_signal
from notify import send_telegram_message
from config import STOCK_SYMBOLS, CRYPTO_SYMBOLS

def process_symbol(symbol, fetch_func, asset_type):
    try:
        df = fetch_func(symbol)
        df = add_indicators(df)
        signal = generate_signal(df)

        msg = (
            f"{asset_type} Signal for {symbol.upper()} on {signal['date']}:\n"
            f"Signal: {signal['signal'].upper()}\n"
            f"RSI: {signal['rsi']:.2f}\n"
            f"MACD Diff: {signal['macd_diff']:.4f}\n"
            f"Volume Spike: {signal['volume_spike']}"
        )
        send_telegram_message(msg)
    except Exception as e:
        print(f"Error processing {symbol}: {e}")

def main():
    print("Running signals for stocks...")
    for symbol in STOCK_SYMBOLS:
        process_symbol(symbol, fetch_stock_data, "Stock")

    print("Running signals for cryptos...")
    for symbol in CRYPTO_SYMBOLS:
        process_symbol(symbol, fetch_crypto_data, "Crypto")

if __name__ == "__main__":
    main()
