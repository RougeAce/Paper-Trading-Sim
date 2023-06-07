from BackEnd import dependines
import yfinance as yf
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







