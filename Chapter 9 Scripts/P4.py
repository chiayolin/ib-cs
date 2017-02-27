# P4.py
#
# Write a Python function named getWeekendAvgTemp that is passed a dictionary 
# of daily temperatures, and returns the average temperature over the weekend 
# for the weekly temperatures given.
#
# date:    02/27/2017
# author:  Chiayo Lin
# license: GPL 3.0

def getWeekendAvgTemp(daily_temp):
    return (daily_temp["sat"] + daily_temp["sun"]) / 2
