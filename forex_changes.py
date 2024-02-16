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
    start_price = hist["Close"].iloc[0]
    end_price = 0

    for data in hist["Close"]:
        prices.append(data)
        prices_count += 1
        prices_sum += data

    end_price = hist["Close"].iloc[prices_count-1]
    total_change = end_price - start_price 
    return {"mean" : (prices_sum / prices_count), "summary" : Summary(prices), "change" : total_change}

def print_increase(data: Summary):
    print("Mean Increase Time: " + str(data["increases"]["mean"]))
    print("Min Increase Time: " + str(data["increases"]["summary"].min))
    print("Q1 Time: " + str(data["increases"]["summary"].Q1))
    print("Median Increase Time: " + str(data["increases"]["summary"].med))
    print("Q3 Time: " + str(data["increases"]["summary"].Q3))
    print("Max Increase Time: " + str(data["increases"]["summary"].max))
    print()

def print_decreases(data: Summary):
    print("Mean Decrease Time: " + str(data["decreases"]["mean"]))
    print("Min Decrease Time: " + str(data["decreases"]["summary"].min))
    print("Q1 Time: " + str(data["decreases"]["summary"].Q1))
    print("Median Decrease Time: " + str(data["decreases"]["summary"].med))
    print("Q3 Time: " + str(data["decreases"]["summary"].Q3))
    print("Max Decrease Time: " + str(data["decreases"]["summary"].max))
    print()

def print_price(data: Summary):
    print("Mean Price: " + str(data["mean"]))
    print("Price Change: " + str(data["change"]))
    print("Lowest Price: " + str(data["summary"].min))
    print("Q1 Price: " + str(data["summary"].Q1))
    print("Median Price: " + str(data["summary"].med))
    print("Q3 Price: " + str(data["summary"].Q3))
    print("Max Price: " + str(data["summary"].max))
    print()

if __name__ == "__main__":
    data = get_hist_data("EUR")
    eur = get_change_summary(data)
    eur_price = get_price_summary(data)

    print()
    print_increase(eur)
    print_decreases(eur)
    print_price(eur_price)