'''
Q: week-by-week with daily update or 
   day-by-day with minute/hour updates?
A: Yes
'''
import tools

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def get_avg_change(hist):
    change_sum = 0

    for i in range(len(hist) - 1):
        start = hist["Close"][i]
        end = hist["Close"][i + 1]
        change_sum += (end - start)

    mean = change_sum / len(hist)
    return mean

# Only works if period = 1 month 
# and interval = 1 day
def get_wbw_stdev(hist):
    num = 0
    weeks = []
    intervals = int(len(hist)/5)

    while (num < intervals):
        currentWeek = []
        for i in range(5):
            index = (num * 5) + i
            currentWeek.append(hist[index])
        
        stdev = tools.stdev(currentWeek)
        weeks.append(stdev)
        num += 1
    
    return tools.mean(weeks) 

# Period = 7d, interval = 1h
def get_dbd_stdev(hist):
    num = 0
    days = []
    intervals = int(len(hist)/12)

    while (num < intervals):
        currentDay = []
        for i in range(12):
            index = (num * 12) + i
            currentDay.append(hist[index])

        stdev = tools.stdev(currentDay)
        days.append(stdev)
        num += 1

    return tools.mean(days)

def get_analysis_info(currency, debug=False):
    week_minute_data = tools.get_hist_data(currency, "5d", "1m")
    week_hour_data = tools.get_hist_data(currency, "7d", "1h")
    month_daily_data = tools.get_hist_data(currency, "1mo", "1d")

    minute_change = get_avg_change(week_minute_data)
    hour_change = get_avg_change(week_hour_data)
    daily_change = get_avg_change(month_daily_data)
    
    min_stdev = tools.stdev(week_minute_data["Close"])
    hour_stdev = tools.stdev(week_hour_data["Close"])
    day_stdev = tools.stdev(month_daily_data["Close"])
    wbw = get_wbw_stdev(month_daily_data["Close"])
    dbd = get_dbd_stdev(week_hour_data["Close"])

    if (debug):
        print("USD/" + currency)
        print("Standard Dev (minute): " + str(round(min_stdev, 5)))
        print("Standard Dev (hour): " + str(round(hour_stdev, 5)))
        print("Standard Dev (day): " + str(round(day_stdev, 5)))
        print("Week-by-Week: " + str(round(wbw, 5)))
        print("Day-by-Day: " + str(round(dbd, 5)))

        print("Average Change (minute): " + str(minute_change))
        print("Average Change (hour): " + str(hour_change))
        print("Average Change (day): " + str(daily_change))

    return {
        "minute_change" : minute_change,
        "hour_change" : hour_change,
        "daily_change" : daily_change,

        "minute_stdev" : min_stdev,
        "hour_stdev" : hour_change,
        "day_stdev" : day_stdev,

        "weekbyweek" : wbw,
        "daybyday" : dbd,

        "stdevs" : [min_stdev, hour_change, day_stdev, wbw, dbd]
    }