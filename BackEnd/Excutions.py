import csv
import CLI

def buy_stock(ticker, amount, price, date, total_transaction_cost, file_path):
    try:
        with open(file_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow((["BUYING", ticker, amount, price, date, total_transaction_cost]))
        return 0

    except:
        return 1


def sell_stock(ticker, amount, price, date, total_transaction_cost, file_path):
    try:
        with open(file_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow((["SELLING", ticker, amount, price, date, total_transaction_cost]))
        return 0

    except:
        return 1