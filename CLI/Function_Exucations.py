from BackEnd import dependines
import yfinance as yf
import csv
from datetime import datetime
import os
from BackEnd import Values
from BackEnd import Excutions
from BackEnd import buying_options
import numpy as np


def check_exceptions(ticker):
    if dependines.is_nyse_open() == False:
        return True
    if dependines.ticker_exists(ticker) == False:
        return 1001
    return True


def buy_stock(ticker, amount, account):
    file_path = f'{account}_STOCKS.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_stock = dependines.stock_value(ticker)
    cost = price_stock * amount
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            if cash == None:
                return 3000 # 3000 means the cash could not be proccesed
            if cash < cost:
                return 4000 #4000 means there is not enough cash to cover the cost
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("STOCK", "BUYING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date
        else:
            cash = 100000
            if cash < cost:
                return 40000
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("STOCK", "BUYING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date




    return 5

def cash_amount(file_path):
    if file_exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 1:
                return lines[-1].strip()
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
    if type == "OPTION":
        fileE = file_exists(file_path)
        with open(file_path, "a") as f:
            writer = csv.writer(f)
            if fileE == False:
                writer.writerow(['TYPE', "ACTION", "ASSET", "COST/ASSET", "Amount", "TOTAL_COST", "CASH_LEFT", "DATE"])

            writer.writerow([type, action, ticker, price, amount, cost, cash, date])
        with open(cash_path, "a") as f:
            writer = csv.writer(f)
            if fileE == False:
                writer.writerow(['CASH'])
            writer.writerow([cash])



def file_exists(file_path):
    return os.path.isfile(file_path)

def cash_buy(ticker, amount, account):
    price = dependines.stock_value(ticker)
    share_amount = amount / price
    return buy_stock(ticker, share_amount, account)

def cash_sell(ticker, amount, account):
    price = dependines.stock_value(ticker)
    share_amount = amount / price
    return sell_stock(ticker, share_amount, account)




##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


def sell_stock(ticker, amount, account):
    file_path = f'{account}_STOCK.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_stock = dependines.stock_value(ticker)
    cost = price_stock * amount
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            stock_amount_owned = total_stocks_owned(file_path, ticker)
            if cash == None:
                return 3000 # 3000 means the cash could not be proccesed
            if amount > stock_amount_owned:
                return 5000 #5000 means there is not enough stocks to cover the cost
            else:
                date = datetime.now()
                cash += cost
                exacute_order("STOCK", "SELLING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return 4, "sold", amount, ticker, cash, cost, date
        else:
            return 5000




    return 5

def total_stocks_owned(file_path, ticker):
    total = 0
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.strip().split(',')
            if data[0] == 'STOCK' and data[2] == ticker:
                if data[1] == 'BUYING':
                    total += float(data[4])
                elif data[1] == 'SELLING':
                    total -= int(data[4])
    return total


def buy_option(ticker, amount, account):
    if dependines.check_option(ticker) == False:
        return 6000 # Means the ticker could not be proccesed
    file_path = f'{account}_STOCKS.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_option = buying_options.cost_options(ticker)
    cost = float(price_option) * float(amount)
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            if cash == None:
                return 3000 # 3000 means the cash could not be proccesed
            if cash < cost:
                return 4000 #4000 means there is not enough cash to cover the cost
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("OPTION", "BUYING", ticker, price_option, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date
        else:
            cash = 100000
            if cash < cost:
                return 40000
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("OPTION", "BUYING", ticker, price_option, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date

def sell_call(ticker, amount, account):
    if dependines.check_option(ticker) == False:
        return 6000 # Means the ticker could not be proccesed
    real_ticker = dependines.option_underlying(ticker)
    file_path = f'{account}_STOCKS.csv'
    cash_path = f'{account}_CASH.csv'
    cash = float(cash_amount(cash_path))
    price = buying_options.cost_options(ticker)
    cost = float(price) * float(amount)
    stock_amount_owned = total_stocks_owned(file_path, ticker)
    if stock_amount_owned > stock_amount_owned:
        return 4000
    cash += float(cost)
    exacute_order("OPTION", "SELLING", ticker, price, amount, cost, cash, datetime.today(), file_path, cash_path)
    return 4, "SOLD", amount, ticker, cash, cost, datetime.today()












def sell_put(ticker, amount, account):
    if dependines.check_option(ticker) == False:
        return 6000  # Means the ticker could not be proccesed
    real_ticker = dependines.option_underlying(ticker)
    file_path = f'{account}_STOCKS.csv'
    cash_path = f'{account}_CASH.csv'
    cash = float(cash_amount(cash_path))
    price = buying_options.cost_options(ticker)
    cost = float(price) * float(amount)
    if (real_ticker * 100 * amount) > cash:
        return 4000
    cash += float(cost)
    exacute_order("OPTION", "SELLING", ticker, price, amount, cost, cash, datetime.today(), file_path, cash_path)
    return 4, "SOLD", amount, ticker, cash, cost, datetime.today()

import csv
import numpy as np

def calculate_account_value(account):
    print(account)
    stock_file = f"{account}_STOCKS.csv"
    cash_file = f"{account}_CASH.csv"
    cash = 0

    with open(stock_file, "r") as f:
        csv_reader = csv.reader(f)
        # [TYPE,ACTION,ASSET,COST/ASSET,Amount,TOTAL_COST,CASH_LEFT,DATE]
        for row in csv_reader:
            if row[1] == "BUYING":
                ticker = row[2]
                value = np.float64(dependines.stock_value(ticker)) * np.float64(row[4])
                if row[0] == "OPTION":
                    value *= 100
                cash += value
            elif row[1] == "SELLING":  # Fixed index from 2 to 1
                ticker = row[2]
                value = np.float64(dependines.stock_value(ticker)) * np.float64(row[4])
                if row[0] == "OPTION":
                    value *= 100
                cash -= value

    cash += float(cash_amount(cash_file))
    return cash













##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


def sell_stock(ticker, amount, account):
    file_path = f'{account}_STOCK.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_stock = 170
    cost = price_stock * amount
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            stock_amount_owned = total_stocks_owned(file_path, ticker)
            if cash == None:
                return 3000 # 3000 means the cash could not be proccesed
            if amount > stock_amount_owned:
                return 5000 #5000 means there is not enough stocks to cover the cost
            else:
                date = datetime.now()
                cash += cost
                exacute_order("STOCK", "SELLING", ticker, price_stock, amount, cost, cash, date, file_path, cash_path)
                return 4, "sold", amount, ticker, cash, cost, date
        else:
            return 5000




    return 5

def total_stocks_owned(file_path, ticker):
    total = 0
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.strip().split(',')
            if data[0] == 'STOCK' and data[2] == ticker:
                if data[1] == 'BUYING':
                    total += int(data[4])
                elif data[1] == 'SELLING':
                    total -= int(data[4])
    return total


def buy_option(ticker, amount, account):
    file_path = f'{account}_STOCK.csv'
    cash_path = f'{account}_CASH.csv'
    # Get the necceray information for this portoflio to work
    price_option = 170 
    price_stock = 170
    cost = price_stock * amount * 100
    if check_exceptions(ticker):
        if file_exists(cash_path):
            cash = float(cash_amount(cash_path))
            if cash == None:
                return 3000 # 3000 means the cash could not be proccesed
            if cash < cost:
                return 4000 #4000 means there is not enough cash to cover the cost
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("OPTION", "BUYING", ticker, price_option, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date
        else:
            cash = 100000
            if cash < cost:
                return 40000
            else:
                date = datetime.now()
                cash -= cost
                exacute_order("OPTION", "BUYING", ticker, price_option, amount, cost, cash, date, file_path, cash_path)
                return 4, "bought", amount, ticker, cash, cost, date




    return 5







