import yfinance as yf

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def get_hist_data(ticker, period, interval):
    curr = yf.Ticker(ticker)
    hist = curr.history(period=period, interval=interval)
    return hist

def get_current_exchange(ticker):
    data = yf.Ticker(ticker)
    return data.info["bid"]

'''
TODO: CARTER

write something which takes get_hist_data() and writes 
it to a .json file. JSON file should have a name simiilar
to "hist_EURUSD.json" (just insert ticker into filename).

'''