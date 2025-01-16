import pandas as pd
import requests


headers = {"User-Agent": "lukasjakstas@yahoo.com"}

def cik_matching_ticker(ticker, header = headers):
    ticker = ticker.upper().replace(".", "-")
    ticker_json = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers).json()

    for company in ticker_json.values():
        if(company["ticker"] == ticker):
            cik = str(company["cik_str"]).zfill(10)
            return cik
    raise ValueError(f"Ticker {ticker} not found in SEC database")
