import yfinance as yf
from time import sleep

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

changes = {}

# Get initial prices
for code in currencyCodes:
    data = yf.Ticker("USD" + code + "=X")
    price = data.info['bid']

    changes["USD" + code] = price

for i in range(10):
    sleep(60)
    print("Minute " + str(i))
    for code in currencyCodes:
        data = yf.Ticker("USD" + code + "=X")
        price = data.info['bid']

        if (price > changes["USD" + code]):
            print("Price increase for USD/" + code)

    print()
