import math
import yfinance as yf

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def mean(set):
    size = len(set)
    sum = 0
    for i in range(size):
        sum += set[i]
    sum = sum / size
    return sum

def stdev(set):
    difference = 0
    avg = mean(set)
    size = len(set)
    for i in range(size):
        difference += ((set[i] - avg) ** 2)
    sd = math.sqrt(difference / size)
    return sd

# Top 20 world currencies
currencyCodes = [
    'EUR',      # Euro
    'JPY',      # Japan
    'GBP',      # UK 
    'CNY',      # China
    'AUD',      # Australia
    'CAD',      # Canada
    'CHF',      # Swiss
    'HKD',      # Hong Kong
    'SGD',      # Singapore
    'SEK',      # Swedian
    'KRW',      # South Korea
    'NOK',      # Norway
    'NZD',      # New Zealand
    'INR',      # India
    'MXN',      # Mexico
    'TWD',      # Taiwan
    'ZAR',      # South Africa
    'BRL',      # Brazil
    'DKK'       # Denmark
]

def get_hist_data(code, period, interval):
    curr = yf.Ticker(code + "USD=X")
    hist = curr.history(period=period, interval=interval)
    return hist
