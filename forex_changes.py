import yfinance as yf
from tools import get_hist_data

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

class Summary:
    def __init__(self, data):
        data.sort()
        self.data_len = len(data)

        self.min = data[1]
        self.Q1 = data[ int(self.data_len / 4) ]
        self.med = data[ int(self.data_len / 2) ]
        self.Q3 = data[ int(3 * (self.data_len / 4)) ]
        self.max = data[ self.data_len - 1 ]

def get_change_summary(hist):
    # For loop
    state = "decreasing"        # Will be caught by first if statement
    lastValue = 0
    minuteCount = 0
    
    # Data
    inc_lengths = []
    inc_sum = 0

    dec_lengths = []
    dec_sum = 0

    for data in hist["Close"]:
        if (data >= lastValue and state == "decreasing"):
            dec_lengths.append(minuteCount)
            dec_sum += minuteCount
            minuteCount = 0
            state = "increasing"

        elif (data < lastValue and state == "increasing"):
            inc_lengths.append(minuteCount)
            inc_sum += minuteCount
            minuteCount = 0
            state = "decreasing"

        minuteCount += 1
        lastValue = data

    return {
        "increases" : {
            "mean" : (inc_sum / len(inc_lengths)), "summary" : Summary(inc_lengths)
        },
        "decreases" : {
            "mean" : (dec_sum / len(dec_lengths)), "summary" : Summary(dec_lengths) 
        }
    }    

def get_price_summary(hist):
    # Increase price data
    prices = []
    prices_count = 0
    prices_sum = 0
    start_price = hist["Close"].iloc[0]     # .iloc prevents futurewarning with pandas?
    end_price = 0

    for data in hist["Close"]:
        prices.append(data)
        prices_count += 1
        prices_sum += data

    end_price = hist["Close"].iloc[prices_count-1]
    total_change = end_price - start_price 
    return {"mean" : (prices_sum / prices_count), "summary" : Summary(prices), "change" : total_change}

def print_summary(data):
    print("Mean: " + str(data["mean"]))
    print("Min: " + str(data["summary"].min))
    print("Q1: " + str(data["summary"].Q1))
    print("Median: " + str(data["summary"].med))
    print("Q3: " + str(data["summary"].Q3))
    print("Max: " + str(data["summary"].max))
    print()

# Remove this 
def get_changes_info(currency, debug=False):
    data = get_hist_data(currency, "5d", "1m")
    changes = get_change_summary(data)
    price_info = get_price_summary(data)

    if (debug):
        print()
        print("Increases:")
        print_summary(changes["increases"])
    
        print("Decreases")
        print_summary(changes["decreases"])
    
        print("Price")
        print("Overall Price Change: " + str(price_info["change"]))
        print_summary(price_info)

    return {
        "changes" : changes,
        "price_info" : price_info
    }