'''
TODO
how to weight different statistics? 
We need to look at 1month,5day change (?)
'''

import tools
from forex_analysis import *
from forex_changes import *

import yfinance as yf

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

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
            data = yf.Ticker(code + "USD=X")
            price = data.info["bid"]
            self.exchange_rates[code + "USD"] = price

    def get_currency_data(self, currency):
        self.get_exchange_rates()
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
        change_data = data["change"]["changes"]

        sdsum = 0
        for sd in analysis_data["stdevs"]:
            sdsum += sd

        a = 0.1
        b = 5
        c = 5

        # The big deal
        score = (
            1 + (a * (sdsum)/5)
            + b * (change_data["increases"]["summary"].med - change_data["decreases"]["summary"].med)
            + c * (change_data["increases"]["mean"] - change_data["decreases"]["mean"])
        )

        print(currency + " Score : " + str(score))

if __name__ == "__main__":
    #test_analysis = get_analysis_info("EUR", debug=True)
    #test_changes = get_changes_info("EUR", debug=True)
    #print()

    dickbutt = Model(100)
    for code in tools.currencyCodes:
        dickbutt.get_score(code)