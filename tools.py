import math
import numpy as np

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

def get_mean(set):
    '''
    size = len(set)
    sum = 0
    for i in range(size):
        sum += set[i]
    sum = sum / size
    return sum
    '''
    return np.mean(set)
    
def get_stdev(set):
    '''
    difference = 0
    avg = get_mean(set)
    size = len(set)
    for i in range(size):
        difference += ((set[i] - avg) ** 2)
    sd = math.sqrt(difference / size)
    return sd
    '''
    return np.std(set)
    
def pivotpoint(high, low, close):
    pp = (high + low + close) / 3 
    return pp

def get_resistances(rlev, high, low, pp):
    r = 0
    if rlev == 1:
        r = (2 * pp) - low
    elif rlev == 2:
        r = pp + (high - low)
    elif rlev == 3:
        r = high + 2 * (high - pp)
    return r

def get_supports(slev, high, low, pp):
    s = 0
    if slev == 1:
        s = (2 * pp) - high
    elif slev == 2:
        s = pp - (high - low)
    elif slev == 3:
        s = low - 2 * (high - pp)
    return s