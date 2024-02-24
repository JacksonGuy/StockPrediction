import yfinance as yf
from datetime import datetime

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def get_hist_data(ticker, period="5d", interval="1m"):
    curr = yf.Ticker(ticker)
    dates = get_date_range()
    hist = curr.history(period=period, interval=interval, 
                        start = dates["start"], end = dates["end"])
    return hist

def get_date_range():
    today = datetime.today()
    start = today.day - 8
    end = today.day - 1
    startDate = "{}-{}-{}".format(today.year, today.month, start)
    endDate = "{}-{}-{}".format(today.year, today.month, end)
    return {"start" : startDate, "end" : endDate}

def get_current_exchange(ticker):
    data = yf.Ticker(ticker)
    return data.info["bid"]

'''
TODO: CARTER

write something which takes get_hist_data() and writes 
it to a .json file. JSON file should have a name simiilar
to "hist_EURUSD.json" (just insert ticker into filename).

'''
