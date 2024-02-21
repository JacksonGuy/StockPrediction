'''
TODO
how to weight different statistics? 
We need to look at 1month,5day change (?)
rename wbw and dbd variables and functions
split data up for simulations 
how the fuck to deal with different trade periods 
    - will different markets being closed affect which
      currencies that we can trade to?
'''

import tools
from forex_analysis import *
from forex_changes import *

class Model:
    exchange_rates = {}
    currency_stats = {}
    currency_scores = {}

    start_money = 0         # in USD
    balance = 0
    portfolio = {}          # Currencies invested in

    def __init__(self, start_money):
        self.start_money = start_money
        self.balance = start_money

    def get_currency_data(self, currency):
        analysis_data = get_analysis_info(currency)
        change_data = get_changes_info(currency)
        self.currency_stats[currency] = {
            "analysis" : analysis_data,
            "change" : change_data
        }

    def get_score(self, currency, debug = False):
        self.get_currency_data(currency)
        data = self.currency_stats[currency]
        analysis_data = data["analysis"]
        change_data = data["change"]["changes"]

        sdsum = 0
        for sd in analysis_data["stdevs"]:
            sdsum += sd

        a = 10
        b = 2
        c = 2

        # The big deal
        score = (
            1 + (a * (sdsum))
            + b * (change_data["increases"]["summary"].med - change_data["decreases"]["summary"].med)
            + c * (change_data["increases"]["mean"] - change_data["decreases"]["mean"])
        )

        if (debug):
            print(currency + " Score : " + str(score))

        self.currency_scores[currency] = score

    def get_currency_scores(self, debug = False):
        for code in tools.currencyCodes:
            self.get_score(code, debug)

    def get_best_score(self):
        best = 0
        returnVal = ""
        for curr in self.currency_scores:
            if (self.currency_scores[curr] > best):
                best = self.currency_scores[curr]
                returnVal = curr
        return returnVal
    
    # sim_data should have intervals of 1 minute for some period of time
    # Recommended is 1-3 days
    def run_simulation(self, period):
        print("\n\nStarted Simulation")
        
        print("Gathering Data...")
        sim_data = {}
        for code in tools.currencyCodes:
            sim_data[code] = tools.get_hist_data(code, period, "1m")
        
        decrease_ticker = 0

        print("Simulating...")
        for curr in sim_data:
            if (len(sim_data[curr]) == 1):
                print(curr)
                print(sim_data[curr])

        print("Done")

if __name__ == "__main__":
    dickbutt = Model(100)
    dickbutt.get_exchange_rates()
    dickbutt.get_currency_scores()

    best = dickbutt.get_best_score()
    print("Best currency: " + best)
    print("Score: " + str(dickbutt.currency_scores[best]))

    # Buy best
    dickbutt.portfolio[best] = dickbutt.balance * dickbutt.exchange_rates["USD" + best]

    dickbutt.run_simulation("1d")