from BackEnd import dependines
import csv
from datetime import datetime
import os
from BackEnd import Values
from BackEnd import Excutions


def check_exceptions(ticker):
    if dependines.is_nyse_open() == False:
        return True
    if dependines.ticker_exists(ticker) == False:
        return 1001
    return True


def buy_stock(ticker, amount, account):
    file_path = f'{account}_STOCK.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_stock = 170
    cost = price_stock * amount
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            if cash < cost:
                return 4000 #4000 means there is not enough cash to cover the cost
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("STOCK", "BUYING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return True
        else:
            cash = 100000
            if cash < cost:
                return 40000
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("STOCK", "BUYING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return True




    return False

def cash_amount(file_path):
    if file_exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                return lines[1].strip()
    else:
        with open(file_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["CASH"])
            writer.writerow(["100000"])
    return 100000

def exacute_order(type, action, ticker, price, amount,cost, cash, date,file_path, cash_path):
    if type == "STOCK":
        fileE = file_exists(file_path)
        with open(file_path, "a") as f:
            writer = csv.writer(f)
            if fileE == False:
                writer.writerow(['TYPE', "ACTION", "ASSET", "COST/ASSET", "Amount","TOTAL_COST", "CASH_LEFT", "DATE"])
            writer.writerow([type, action, ticker, price, amount, cost, cash, date])

        with open(cash_path, "a") as f:
            writer = csv.writer(f)
            if fileE == False:
                writer.writerow(['CASH'])
            writer.writerow([cash])



def file_exists(file_path):
    return os.path.isfile(file_path)










