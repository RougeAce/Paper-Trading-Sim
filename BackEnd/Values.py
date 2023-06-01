import csv
import yfinance as yf

def calculate_account_value(file_path):
    total_value = 0
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ticker = row['TICKER']
            amount = int(row['AMOUNT'])
            stock = yf.Ticker(ticker)
            info = stock.info
            current_price = info['currentPrice']
            total_value += current_price * amount
    return total_value


def calculate_ticker_amount(file_path, ticker):
    total_amount = 0
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['TICKER'] == ticker:
                amount = int(row['AMOUNT'])
                total_amount += amount
    return total_amount




def check_cash_account_cash_balance(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['CASH'])

