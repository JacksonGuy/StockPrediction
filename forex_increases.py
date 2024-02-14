import yfinance as yf

# Specify Currency Here
curr = yf.Ticker("USDEUR=X")
hist = curr.history(period="7d", interval="1m")

# Increase duration data
currentEnd = 0
minuteCount = -1
inc_lengths = []
inc_sum = 0
inc_count = 0

# Increase price data
prices = []
prices_count = 0
prices_sum = 0
start_price = hist["Close"][0]
end_price = 0

for data in hist["Close"]:
    if (data >= currentEnd):
        minuteCount += 1
        currentEnd = data
    else:
        #print("Price increased for " + str(minuteCount) + " minutes")
        
        inc_lengths.append(minuteCount)
        inc_sum += minuteCount
        inc_count += 1

        minuteCount = 0
        currentEnd = 0

    prices.append(data)
    prices_count += 1
    prices_sum += data
end_price = hist["Close"][prices_count-1]

inc_lengths.sort()
print("Min Increase Time: " + str(inc_lengths[1]))
print("Average Increase Time: " + str(round(inc_sum / inc_count, 5)))
print("Median Increase Time: " + str(inc_lengths[int(inc_count/2)]))
print("Q1 Time: " + str(inc_lengths[int(inc_count/4)]))
print("Q3 Time: " + str(inc_lengths[int( 3 * (inc_count/4) )]))
print("Max Increase Time: " + str(inc_lengths[inc_count-1]))

print()

prices.sort()
print("Average Price: " + str(prices_sum / prices_count))
print("Price Change: " + str(end_price - start_price))
print("Lowest Price: " + str(prices[0]))
print("Q1 Price: " + str(prices[int(prices_count / 4)]))
print("Median Price: " + str(prices[int(prices_count/2)]))
print("Q3 Price: " + str(prices[int(3 * (prices_count/4))]))
print("Max Price: " + str(prices[prices_count-1]))