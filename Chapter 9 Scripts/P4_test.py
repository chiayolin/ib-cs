# P4.py
#
# Write a Python function named getWeekendAvgTemp that is passed a dictionary 
# of daily temperatures, and returns the average temperature over the weekend 
# for the weekly temperatures given.
#
# date:    02/27/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P4 import getWeekendAvgTemp

week_temp = { "mon" : 70, "tue" : 71, "wed" : 72, "thu" : 90,
              "fri" : 12, "sat" : 11, "sun" : 10 }

print(week_temp)
print(getWeekendAvgTemp(week_temp))
