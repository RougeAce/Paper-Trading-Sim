import pandas_market_calendars as mcal
from datetime import datetime
from pytz import timezone
import yfinance as yf
import os



def is_nyse_open():
    nyse = mcal.get_calendar('NYSE')
    tz = timezone('America/New_York')
    now = datetime.now(tz)

    schedule = nyse.schedule(start_date=now, end_date=now)

    if not schedule.empty:
        market_open = schedule.iloc[0].market_open
        market_close = schedule.iloc[0].market_close
        if market_open <= now < market_close:
            return True
        else:
            return False
    else:
        return False


def ticker_exists(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return True
    except:
        return False

def stock_value(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period="1d")
    spy_price = data["Close"].iloc[-1]
    return spy_price



def check_option(ticker):
    try:
        ticker  = yf.Ticker(ticker)
        ticker.info
        return True
    except:
        return False

def check_type(ticker):
    for i in ticker:
        if i == "P":
            return "put"
        else:
            return "call"

def option_underlying(ticker):
    real_ticker = ""
    for i in ticker:
        try:
            int(i)
            return str(real_ticker)
        except:
            real_ticker += i
    return False













