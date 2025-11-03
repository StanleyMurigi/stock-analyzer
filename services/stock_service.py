import os
import requests
from datetime import datetime

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_data(symbol: str):
    """Fetch stock data from Alpha Vantage."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch stock data")

    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception("Invalid response or symbol not found")

    return data["Time Series (Daily)"]


def summarize_stock(symbol: str, data: dict) -> str:
    """Summarize recent stock performance in natural language."""
    sorted_dates = sorted(data.keys(), reverse=True)
    latest_date = sorted_dates[0]
    prev_date = sorted_dates[1]

    latest_close = float(data[latest_date]["4. close"])
    prev_close = float(data[prev_date]["4. close"])
    change = latest_close - prev_close
    percent_change = (change / prev_close) * 100

    # Determine short-term trend (last 5 days)
    closes = [float(data[d]["4. close"]) for d in sorted_dates[:5]]
    avg_past = sum(closes[1:]) / 4
    trend = "uptrend" if latest_close > avg_past else "downtrend"

    # Build summary
    direction = "up" if change > 0 else "down"
    summary = (
        f"{symbol.upper()} closed at ${latest_close:.2f} on {latest_date}, "
        f"{direction} {abs(percent_change):.2f}% from the previous day. "
        f"The recent trend appears to be a {trend}."
    )

    return summary

