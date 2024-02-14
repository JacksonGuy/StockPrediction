import yfinance as yf

curr = yf.Ticker("USDEUR=X")
hist = curr.history(period="7d", interval="1m")

currentEnd = 0
minuteCount = -1
inc_lengths = []
inc_sum = 0
inc_count = 0
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

inc_lengths.sort()
print("Min Increase Time: " + str(inc_lengths[1]))
print("Average Increase Time: " + str(round(inc_sum / inc_count, 5)))
print("Median Increase Time: " + str(inc_lengths[int(inc_count/2)]))
print("Q1 Time: " + str(inc_lengths[int(inc_count/4)]))
print("Q3 Time: " + str(inc_lengths[int( 3 * (inc_count/4) )]))
print("Max Increase Time: " + str(inc_lengths[inc_count-1]))
