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


def getRecentInsider(ticker, lookback_days=1):
    """
    Retrieve recent insider trades for a given ticker.

    Parameters:
        ticker (str): The stock ticker symbol.
        lookback_days (int, optional): The number of days to look back for insider trades (default is 1).

    Returns:
        pandas.DataFrame: A DataFrame containing the latest insider buys, including columns for dates, shares, 
                          and total value of trades.

    Purpose:
        This function is used to identify notable insider activity for a list of tickers. If significant insider 
        trades are found, the winrate() function can be called for further evaluation of potential investment decisions.
    """
    pass


def winrate(ticker, lookback_days=None):
    """
    Calculate the win rate of a stock after insider trading events.

    Parameters:
        ticker (str): The stock ticker symbol.
        lookback_days (int, optional): The number of days to analyze past insider trades (default is None for all available data).

    Returns:
        float: A decimal value between 0 and 1.0 representing the probability of a bull run after insider trading.

    Purpose:
        This function determines the confidence or risk associated with a stock based on the historical impact of insider 
        trades. Insider trade values are used as weights to minimize the effect of low-value trades on the win rate.
    """
    pass


def analyzeTicker(ticker, lookback_days=1):
    """
    Analyze a stock ticker for insider activity and win rate.

    Parameters:
        ticker (str): The stock ticker symbol.
        lookback_days (int, optional): The number of days to look back for insider trades (default is 1).

    Returns:
        dict: A dictionary with keys 'recent_insider_trades' (DataFrame) and 'winrate' (float), summarizing 
              recent insider activity and the calculated win rate for the stock.

    Purpose:
        This function integrates getRecentInsider() and winrate() to provide a combined analysis of insider activity 
        and potential investment risk/reward for a given stock ticker.
    """
    pass


def getTopInsiderTrades(ticker_list, lookback_days=1, top_n=5):
    """
    Identify the top insider trades across multiple tickers.

    Parameters:
        ticker_list (list): A list of stock ticker symbols to analyze.
        lookback_days (int, optional): The number of days to look back for insider trades (default is 1).
        top_n (int, optional): The number of top trades to return based on total trade value (default is 5).

    Returns:
        pandas.DataFrame: A DataFrame containing the top insider trades across the provided tickers, sorted by trade value.

    Purpose:
        This function compares insider trade data across multiple tickers to identify high-value insider activity 
        that may be indicative of potential investment opportunities.
    """
    pass
