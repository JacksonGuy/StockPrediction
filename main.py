'''
TODO
convert stock_analysis to look at forex data
forex_increases but more flexible
'''

from tools import *
import math
import yfinance as yf

class Investment:
    currency = ""       # Name of the currency (EUR, AUD, etc)
    usd_amout = 0       # How much of that currency in USD

class Model:
    start_money = 0         # in USD
    portfolio = {}          # Currencies invested in

    def __init__(self, start_money):
        self.start_money = start_money

    # Search for good initial trade
    def search_initial(self):
        for code in currencyCodes:
            data = yf.Ticker("USD" + code + "=X")
            price = data.info["bid"]

def main():
    pass

if __name__ == "__main__":
    main()    
