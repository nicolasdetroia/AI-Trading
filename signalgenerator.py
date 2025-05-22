# signal_generator.py
import pandas as pd

def generate_signal(df):
    """
    Generate trading signal for the latest date in df.
    Returns: dict with date, signal, rsi, macd_diff, volume_spike
    """
    latest = df.iloc[-1]

    signal = "hold"
    if latest["rsi"] < 30 and latest["volume_spike"]:
        signal = "buy"
    elif latest["rsi"] > 70 or (latest["macd_diff"] < 0):
        signal = "sell"

    return {
        "date": latest.name.strftime("%Y-%m-%d"),
        "signal": signal,
        "rsi": latest["rsi"],
        "macd_diff": latest["macd_diff"],
        "volume_spike": bool(latest["volume_spike"]),
    }
