# Automatic forex trading bot
# Version 1 

class Investment:
    ticker = ""
    usd_amount = 0

    def __init__(self, ticker, usd_amount):
        self.ticker = ticker
        self.usd_amount = usd_amount

class Model_A:
    # Both of these in USD
    start_money = 0
    balance = 0        

    # key = ticker, value = Investment
    # Ex: "EURUSD" : Investment("EURUSD", 100)
    # Dictionary for quick reference
    portfolio = {}

    # start_money in USD
    def __init__(self, start_money):
        self.start_money = start_money
        self.balance = start_money

    def get_score(self):
        pass

    def simulation(self):
        pass