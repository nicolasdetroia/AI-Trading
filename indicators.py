# indicators.py
import pandas as pd
import ta

def add_indicators(df):
    """
    Add technical indicators to dataframe:
    - RSI (14)
    - SMA (20, 50)
    - EMA (20, 50)
    - MACD (12, 26, 9)
    - Volume spike detection (volume today > 1.5x avg volume 20 days)
    """
    df = df.copy()

    # RSI
    df["rsi"] = ta.momentum.rsi(df["close"], window=14)

    # SMA
    df["sma_20"] = df["close"].rolling(window=20).mean()
    df["sma_50"] = df["close"].rolling(window=50).mean()

    # EMA
    df["ema_20"] = df["close"].ewm(span=20, adjust=False).mean()
    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()

    # MACD
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["macd_diff"] = macd.macd_diff()

    # Volume spike
    df["vol_avg_20"] = df["volume"].rolling(window=20).mean()
    df["volume_spike"] = df["volume"] > 1.5 * df["vol_avg_20"]

    return df
