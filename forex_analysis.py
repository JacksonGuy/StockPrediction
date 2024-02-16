'''
Q: week-by-week with daily update or 
   day-by-day with minute/hour updates?
A: Yes
'''
import tools
import yfinance as yf

def get_avg_change(hist):
    change_sum = 0
    
    for i in range(len(hist)):
        start = hist["Open"].iloc[i]
        end = hist["Close"].iloc[i]
        change_sum += (end - start)
    
    mean = change_sum / len(hist)
    return mean

if __name__ == "__main__":
    hist = tools.get_hist_data("HKD", "7d", "1m")
    print(hist)

    avg_change = get_avg_change(hist)
    print(avg_change)
