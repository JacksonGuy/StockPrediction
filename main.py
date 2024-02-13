'''
TODO:
- Open individual .csv files as console parameter (python ./main.py -f apple.csv)
- Open directory of .csv files (python ./main.py -d ./data/)
'''

import csv
import math
import os

# Price information for a single day
class PricePoint:
    start = 0           # Openning price
    end = 0             # Closing price
    change = 0          # Closing - openning 

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.change = round(end - start, 4)

"""
All relevant data for a .csv file.
Stores PricePoints for each day, and various
statistics on those PricePoints.
"""
class DataFile:
    def __init__(self, filename):
        self.filename = filename            # The name of the .csv file
        self.priceData = []                 # List of PricePoints (each day)
        
        self.avg_change = 0                 # Average amount of change each day.
                                            # Should say whether a stock is more likely
                                            # to increase or decrease in price
        
        self.mean = 0                       # Mean closing price. Mostly used to calculate stdev
        self.stdev = 0                      # Standard Deviation. How volatile a stock's price is.

        self.wbw_stdev = []                 # Week-by-week standard deviation.
                                            # Slightly more refined measure of volatility, since looking
                                            # at the overall stdev doesn't account for "bad weeks".
        
        self.wbw_stdev_avg = 0              # Average week-by-week stdev.


        # Open filename passed when object was created
        with open(filename, mode="r") as file:
            csvFile = csv.DictReader(file)
            for entry in csvFile:
                # Create PricePoint using data from .csv
                start = entry["Open"]
                end = entry["Close/Last"]

                start = float(start[1:])
                end = float(end[1:])

                self.priceData.append(PricePoint(start, end))

        # Calculate total change for the entire set
        self.totalChange = self.priceData[0].end - self.priceData[len(self.priceData)-1].end
        self.totalChange = round(self.totalChange, 4)

    # Gets the average daily change in price.
    def get_avg_change(self):
        c = 0
        for point in self.priceData:
            c += point.change
        c = c / len(self.priceData)
        c = round(c, 4)
        self.avg_change = c

    # Gets the mean daily closing price 
    def get_mean(self):
        avg = 0
        for point in self.priceData:
            avg += point.end
        avg = avg / len(self.priceData)
        avg = round(avg, 4)
        self.mean = avg

    # Gets the standard deviation for daily closing prices
    def get_stdev(self):
        diff = 0
        for point in self.priceData:
            diff += ((point.end - self.mean) ** 2)
        stdev = math.sqrt(diff/len(self.priceData))
        stdev = round(stdev, 4)
        self.stdev = stdev

    # Gets weekly standard deviation
    def get_wbw_stdev(self):
        num = 0             # Used for indexing
        weeks = []          # Each week's stdev

        # Each week should have 5 PricePoints (monday-friday)
        while num <= (len(self.priceData)/5) - 1:
            currentWeek = []    # Each PricePoint for that week
            for i in range(5):
                index = (num * 5) + i
                currentWeek.append(self.priceData[index])
            
            # Calculate mean closing price for the week
            mean = 0
            for day in currentWeek:
                mean += day.end
            mean = mean / len(currentWeek)
            mean = round(mean, 4)
            
            # Find standard deviation
            diff = 0
            for day in currentWeek:
                diff += ((day.end - mean) ** 2)
            stdev = math.sqrt(diff/len(currentWeek))
            stdev = round(stdev, 4)

            weeks.append(stdev)     # Add stdev to array
            num += 1                # Increase index
        self.wbw_stdev = weeks      # Set class variable

        # Find mean of weekly stdevs
        avg = 0
        for week in weeks:
            avg += week
        avg = avg / len(weeks)
        avg = round(avg, 4)
        self.wbw_stdev_avg = avg

'''
All this code does is iterate over all files in a single
directory and calculates the statistics for each file.

This isn't really an ideal way of doing things, especially
if we want to use any of this code for practical purposes.
'''

directory = os.fsencode("./data/")                  # Assuming all .csv files are in one directory
files = []                                          # List of files
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):                   # Ensure file is a .csv file
        newFile = DataFile("./data/" + filename)    # Open file
        files.append(newFile)

# Iterate over all files we opened
for file in files:
    file.get_avg_change()
    file.get_mean()
    file.get_stdev()
    file.get_wbw_stdev()

    # Print relevant information
    print(file.filename)
    print("Average Change Per Day: " + str(file.avg_change))
    print("Total Change: " + str(file.totalChange))
    print("STDEV: " + str(file.stdev))

    # Prints each weeks stdev individually
    # Kinda floods the console with data
    #print("Week-by-Week STDEV:")
    #for i in range(len(file.wbw_stdev)):
    #    print("Week " + str(i) + ": " + str(file.wbw_stdev[i]))
    
    print("Week-by-Week STDEV: " + str(file.wbw_stdev_avg))
    print() # Newline