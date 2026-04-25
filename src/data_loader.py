import yfinance as yf
import os 
import pandas as pd

DIRECTORY = "data/raw"

def downloadData(ticker, start, end):
    data = yf.download(ticker,start=start,end=end)
    return data 

def saveRawData(data, ticker):
    os.makedirs(DIRECTORY, exist_ok=True)
    filepath = os.path.join(DIRECTORY, f"{ticker.upper()}_raw.csv")
    data.to_csv(filepath, index=False)

def loadRawData(ticker):

    filepath = os.path.join(DIRECTORY, f"{ticker.upper()}_raw.csv")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No raw data file found for ticker: {ticker}")

    data = pd.read_csv(filepath)

    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"])

    return data