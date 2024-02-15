import yfinance as yf

class Summary:
    def __init__(self, data):
        data.sort()
        self.data_len = len(data)
        self.min = data[1]
        self.Q1 = data[ int(self.data_len / 4) ]
        self.med = data[ int(self.data_len / 2) ]
        self.Q3 = data[ int(3 * (self.data_len / 4)) ]
        self.max = data[ self.data_len - 1 ]

def get_hist_data(code):
    curr = yf.Ticker("USD" + code + "=X")
    hist = curr.history(period="7d", interval="1m")
    return hist

def get_inc_summary(hist):
    # For counting 
    currentEnd = 0
    minuteCount = -1
    
    # Data
    inc_lengths = []
    inc_sum = 0
    inc_count = 0

    for data in hist["Close"]:
        if (data >= currentEnd):
            minuteCount += 1
            currentEnd = data
        else:
            inc_lengths.append(minuteCount)
            inc_sum += minuteCount
            inc_count += 1

            minuteCount = 0
            currentEnd = 0
    return {"mean" : (inc_sum / inc_count), "summary" : Summary(inc_lengths)}    

def get_price_summary(hist):
    # Increase price data
    prices = []
    prices_count = 0
    prices_sum = 0
    start_price = hist["Close"].iloc[0]
    end_price = 0

    for data in hist["Close"]:
        prices.append(data)
        prices_count += 1
        prices_sum += data

    end_price = hist["Close"].iloc[prices_count-1]
    total_change = end_price - start_price 
    return {"mean" : (prices_sum / prices_count), "summary" : Summary(prices), "change" : total_change}

data = get_hist_data("EUR")
eur_inc = get_inc_summary(data)
eur_price = get_price_summary(data)

print("Mean Increase Time: " + str(eur_inc["mean"]))
print("Min Increase Time: " + str(eur_inc["summary"].min))
print("Q1 Time: " + str(eur_inc["summary"].Q1))
print("Median Increase Time: " + str(eur_inc["summary"].med))
print("Q3 Time: " + str(eur_inc["summary"].Q3))
print("Max Increase Time: " + str(eur_inc["summary"].max))

print()

print("Mean Price: " + str(eur_price["mean"]))
print("Price Change: " + str(eur_price["change"]))
print("Lowest Price: " + str(eur_price["summary"].min))
print("Q1 Price: " + str(eur_price["summary"].Q1))
print("Median Price: " + str(eur_price["summary"].med))
print("Q3 Price: " + str(eur_price["summary"].Q3))
print("Max Price: " + str(eur_price["summary"].max))
