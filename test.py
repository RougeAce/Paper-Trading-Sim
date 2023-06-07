import yfinance as yf

def get_price_ticker(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period="1m")
    spy_price = data["Close"].iloc[-1]
    return spy_price

spy_price = get_spy_price()
print("Current price of SPY:", spy_price)
