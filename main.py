
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_stock_data(ticker, period="1y"):
    data = yf.download(ticker, period=period)
    return data

def plot_stock_data(data, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Close"], label="Close Price")
    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{ticker}_stock_price.png")
    print(f"Saved {ticker}_stock_price.png")

if __name__ == "__main__":
    ticker = "AAPL"
    stock_data = get_stock_data(ticker)
    if not stock_data.empty:
        plot_stock_data(stock_data, ticker)
    else:
        print(f"Could not retrieve data for {ticker}")
