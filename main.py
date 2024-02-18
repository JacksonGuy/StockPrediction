'''
TODO
how to weight different statistics? 
'''

import tools
from forex_analysis import *
from forex_changes import *

import math
import yfinance as yf

class Investment:
    currency = ""       # Name of the currency (EUR, AUD, etc)
    usd_amout = 0       # How much of that currency in USD

class Model:
    exchange_rates = {}
    currency_stats = {}

    start_money = 0         # in USD
    portfolio = {}          # Currencies invested in

    def __init__(self, start_money):
        self.start_money = start_money

    # Get information for buying trades
    def get_exchange_rates(self):
        for code in tools.currencyCodes:
            data = yf.Ticker("USD" + code + "=X")
            price = data.info["bid"]
            self.exchange_rates["USD" + code] = price

    def get_currency_data(self, currency):
        analysis_data = get_analysis_info(currency)
        change_data = get_changes_info(currency)
        self.currency_stats[currency] = {
            "analysis" : analysis_data,
            "change" : change_data
        }

    def get_score(self, currency):
        self.get_currency_data(currency)
        data = self.currency_stats[currency]
        analysis_data = data["analysis"]
        change_data = data["change"]

        sdsum = 0
        for sd in data["analysis"]["stdevs"]:
            sdsum += sd

        a = 10
        b = 1
        c = 1

        # The big deal
        score = 1 + (a * sdsum) 
        + b * (change_data["changes"]["increases"]["summary"].med - change_data["changes"]["decreases"]["summary"].med)
        + c * (change_data["changes"]["increases"]["mean"] - change_data["changes"]["decreases"]["mean"])

        print(currency + " Score : " + str(score))

if __name__ == "__main__":
    dickbutt = Model(100)
    for code in tools.currencyCodes:
        dickbutt.get_score(code)