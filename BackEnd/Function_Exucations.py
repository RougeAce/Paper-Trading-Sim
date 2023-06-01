from BackEnd import dependines
import csv
from datetime import datetime
import os

def check_exceptions(ticker):
    if dependines.is_nyse_open() == False:
        return 1000
    if dependines.ticker_exists(ticker) == False:
        return 1001
    return 0

def buy_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    price = dependines.stock_value(ticker)
    if exception_code != 0:
        return exception_code
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        file_path = f"{account}_stocks.csv"
        if os.path.exists(file_path):
            add_stock_file("SELLING", ticker, amount, date, price, file_path)
        else:
            create_stock_file("SELLING", ticker, amount, date, price, file_path)


def sell_stock(ticker, amount, account):
    exception_code = check_exceptions(ticker)
    price = dependines.stock_value(ticker)
    if exception_code != 0:
        return exception_code
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        file_path = f"{account}_stocks.csv"
        if os.path.exists(file_path):
            add_stock_file("SELLING", ticker, amount, date, price, file_path)
        else:
            create_stock_file("SELLING", ticker, amount, date, price, file_path)



def create_stock_file(action, ticker,amount, date, price, file_path):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["ACTION", "TICKER", "AMOUNT", "DATE", "PRICE"])
        writer.writerow([action, ticker, amount, date, price])
    return 0

def add_stock_file(action, ticker,amount, date, price, file_path):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["ACTION", "TICKER", "AMOUNT", "DATE", "PRICE"])
        writer.writerow([action, ticker, amount, date, price])
    return 0

def calculate_account_value(file_path):
    total_value = 0
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ticker = row['TICKER']
            amount = int(row['AMOUNT'])
            value = dependines.stock_value(ticker)
            total_value += value * amount
    return total_value








