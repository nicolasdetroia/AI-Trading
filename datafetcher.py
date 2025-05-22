# data_fetcher.py
import requests
import pandas as pd
from config import ALPHA_VANTAGE_API_KEY, COINGECKO_API_BASE

def fetch_stock_data(symbol):
    """
    Fetch daily stock data from Alpha Vantage API.
    Returns a DataFrame with Date index and columns: open, high, low, close, volume.
    """
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
    )
    r = requests.get(url)
    data = r.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"Error fetching stock data for {symbol}: {data.get('Error Message', 'Unknown error')}")

    ts = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(ts, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "6. volume": "volume",
    })[["open", "high", "low", "close", "6. volume"]]

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["6. volume"].astype(float)
    df = df.drop(columns=["6. volume"])

    return df

def fetch_crypto_data(symbol):
    """
    Fetch daily crypto data from CoinGecko API.
    symbol: CoinGecko coin id (e.g. 'bitcoin')
    Returns DataFrame with date index and columns: open, high, low, close, volume
    """
    url = f"{COINGECKO_API_BASE}/coins/{symbol}/market_chart?vs_currency=usd&days=90&interval=daily"
    r = requests.get(url)
    data = r.json()

    if "prices" not in data:
        raise Exception(f"Error fetching crypto data for {symbol}")

    prices = data["prices"]  # [timestamp, price]
    market_caps = data.get("market_caps", [])
    volumes = data.get("total_volumes", [])

    # Convert to DataFrame
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.set_index("timestamp")

    # For OHLC approximation from daily price points, use close price as price (CoinGecko provides only price per day)
    # CoinGecko does not provide OHLC directly via free API; here, use price as close
    df["open"] = df["price"]
    df["high"] = df["price"]
    df["low"] = df["price"]
    df["close"] = df["price"]

    # Volume
    vol_df = pd.DataFrame(volumes, columns=["timestamp", "volume"])
    vol_df["timestamp"] = pd.to_datetime(vol_df["timestamp"], unit="ms")
    vol_df = vol_df.set_index("timestamp")

    df = df.join(vol_df["volume"], how="left")
    df = df.drop(columns=["price"])
    df = df.dropna()

    return df

if __name__ == "__main__":
    # Quick test:
    print("Fetching AAPL data...")
    df_stock = fetch_stock_data("AAPL")
    print(df_stock.tail())

    print("Fetching Bitcoin data...")
    df_crypto = fetch_crypto_data("bitcoin")
    print(df_crypto.tail())
