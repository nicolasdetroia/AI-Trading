# AI Trading

# AI-Powered Swing Trading Signal Generator

## Overview
This is a simple Python-based tool designed to help you identify long-term and swing trading opportunities in **stocks** and **cryptocurrencies** using technical indicators and AI models. It fetches daily market data, computes key indicators, runs trading signal logic (rule-based and/or ML models), and sends you timely notifications when buy or sell conditions are met.

The focus is on **stocks and crypto** with a **long-term/swing trading horizon**, making it suitable for traders who prefer holding positions over days or weeks rather than day trading.

---

## Features

- Fetches daily OHLCV (Open, High, Low, Close, Volume) data for stocks and cryptocurrencies from free public APIs (Alpha Vantage, Finnhub, CoinGecko, Binance).
- Calculates key technical indicators:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Simple and Exponential Moving Averages (SMA, EMA)
  - Volume spike detection
  - Price momentum
- Applies trading signal rules or ML model predictions to generate buy, sell, or hold signals.
- Sends notifications with actionable alerts via Telegram or Email.
- Easily customizable symbol watchlist.
- Scheduled to run daily or weekly, automating your market monitoring.
  
---

## Getting Started

### Prerequisites
- Python 3.8+
- API keys for:
  - [Alpha Vantage](https://www.alphavantage.co/) (stocks)
  - [Finnhub](https://finnhub.io/) (stocks, optional)
  - [CoinGecko](https://www.coingecko.com/en/api) or Binance API (crypto)
- Telegram bot token and chat ID **OR** Email SMTP credentials for notifications.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-swing-trading-signals.git
   cd ai-swing-trading-signals
