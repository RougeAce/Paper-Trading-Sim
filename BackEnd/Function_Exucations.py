from BackEnd import dependines
import csv
from datetime import datetime
import os
from BackEnd import Values

def check_exceptions(ticker):
    if dependines.is_nyse_open() == False:
        return 1000
    if dependines.ticker_exists(ticker) == False:
        return 1001
    return 0

def sell_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    price = dependines.stock_value(ticker)
    file_path = f"{account}_stocks.csv"
    file_exists = os.path.exists(file_path)
    date = datetime.now().strftime("%Y-%m-%d")
    holdings = stock_amount_holding(file_path, ticker)




    if exception_code != 0:
        return exception_code
    elif file_exists == False:
        create_stock_file("SELLING", ticker, amount, date, price, file_path)
        if holdings > 100000:
            return 4000

    elif file_exists == True:
        if holdings < amount:
            return 4000


def buy_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    price = dependines.stock_value(ticker)
    file_path = f"{account}_stocks.csv"
    cash_path = f"{account}_CASH.csv"
    file_exists = os.path.exists(file_path)
    date = datetime.now().strftime("%Y-%m-%d")


    if exception_code != 0:
        return exception_code


    elif file_exists == False:
        if amount * price > 100000:
            create_stock_file("BUYING", ticker, amount, date, price, file_path)
            create_cash_account(file_path)
        else:
            return 4000


    elif file_exists == True:
        if amount * price > check_cash(file_path):
            return 4000







def create_stock_file(action, ticker,amount, date, price, file_path):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["ACTION", "TICKER", "AMOUNT", "DATE", "PRICE"])
        writer.writerow([action, ticker, amount, date, price])
    return 0

def add_stock_file(action, ticker,amount, date, price, file_path):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow([action, ticker, amount, date, price])
    return 0



def calculate_account_value(file_path):
    return Values.calculate_account_value(file_path)

def stock_amount_holding(file_path, ticker):
    return Values.calculate_ticker_amount(file_path, ticker)

def create_cash_account(file_path):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["CASH"])
        writer.writerow(['100000'])
    return 0

def check_cash(file_path):
    Values.check_cash_account_cash_balance(file_path)






