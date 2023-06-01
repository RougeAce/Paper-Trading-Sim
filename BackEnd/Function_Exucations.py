import dependines
import csv
from datetime import datetime

def check_exceptions(ticker):
    if dependines.is_nyse_open() == False:
        return 1000
    if dependines.ticker_exists(ticker) == False:
        return 1001
    return 0

def buy_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    if exception_code != 0:
        return exception_code
    else:
        with open(f"{account}_stocks.csv", "a") as f:
            writer = csv.writer(f)
            date = datetime.now().strftime("%Y-%m-%d")
            writer.writerow(["BUYING", ticker, amount, date])
        return 0


def sell_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    if exception_code != 0:
        return exception_code
    else:
        with open(f"{account}_stocks.csv", "a") as f:
            writer = csv.writer(f)
            date = datetime.now().strftime("%Y-%m-%d")
            writer.writerow(["SELLING", ticker, amount, date])
        return 0






