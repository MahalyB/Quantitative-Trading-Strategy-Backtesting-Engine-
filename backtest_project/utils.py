# download ticker data for NVDA over past 7 year period
import yfinance as yf
import os
import time

def download_data(ticker, start="2018-01-01", end="2025-01-01", save=True):
    data = yf.download(ticker, start=start, end=end)
    if save:
        os.makedirs("data", exist_ok=True)
        data.to_csv(f"data/data{ticker}.csv")

    return data

ticker_list = ["NVDA", "AAPL", "TSLA", "AMD", "INTC", "QCOM", "MSFT", "GOOGL", "AMZN", "META"]

for ticker in ticker_list:
    print(f"Downloading data for {ticker}")
    download_data(ticker)
    time.sleep(1)