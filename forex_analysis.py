'''
Q: week-by-week with daily update or 
   day-by-day with minute/hour updates?
A: Yes
'''
import tools
import yfinance as yf

def get_avg_change(hist):
    change_sum = 0

    for i in range(len(hist) - 1):
        start = hist["Close"].iloc[i]
        end = hist["Close"].iloc[i + 1]
        change_sum += (end - start)

    mean = change_sum / len(hist)
    return mean

def get_wbw_stdev(hist):
    pass

if __name__ == "__main__":
    currency = "AUD"
    week_minute_data = tools.get_hist_data(currency, "7d", "1m")
    week_hour_data = tools.get_hist_data(currency, "7d", "1h")
    month_daily_data = tools.get_hist_data(currency, "1mo", "1d")

    minute_change = get_avg_change(week_minute_data)
    hour_change = get_avg_change(week_hour_data)
    daily_change = get_avg_change(month_daily_data)
    
    min_stdev = tools.stdev(week_minute_data["Close"])
    hour_stdev = tools.stdev(week_hour_data["Close"])
    day_stdev = tools.stdev(month_daily_data["Close"])
    
    print()
    print("USD/" + currency)
    print("Standard Dev (minute): " + str(round(min_stdev, 5)))
    print("Standard Dev (hour): " + str(round(hour_stdev, 5)))
    print("Standard Dev (day): " + str(round(day_stdev, 5)))

    print("Average Change (minute): " + str(minute_change))
    print("Average Change (hour): " + str(hour_change))
    print("Average Change (day): " + str(daily_change))