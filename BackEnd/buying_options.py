import yfinance as yf
import csv
import CLI

ticker = ("AAPL230609P00180000")



def options_stirke_price(ticker, amount):
    return yf.Ticker(ticker).info['strikePrice'] * amount

def cost_options(ticker):
    return yf.Ticker("AAPL230609C00180000").info['regularMarketPreviousClose']  * 100

print("Hello World")
