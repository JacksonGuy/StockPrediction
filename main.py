'''
TODO
convert stock_analysis to look at forex data
might have to change forex_change to do open-to-close instead
    of close-to-close
'''

import tools
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
        for code in tools.currencyCodes:
            data = yf.Ticker("USD" + code + "=X")
            price = data.info["bid"]

def main():
    pass

if __name__ == "__main__":
    main()    
