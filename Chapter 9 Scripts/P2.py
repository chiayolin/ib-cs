# P2.py
#
# Write a Python function named moderateDays that is given a dictionary
# containing the average daily temperature for each day of a week, and 
# returns a list of the days in which the average temperature was 
# between 70 and 79 degrees. Write a program that demonstrates the 
# function. 
#
# date:    02/27/2017
# author:  Chiayo Lin
# license: GPL 3.0

def moderateDays(week_temps):
    moderate_days = []
    for day in ("mon", "tue", "wed", "thu", "fri", "sat", "sun"):
        if week_temps[day] in range(70, 80):
            moderate_days += [day]

    return moderate_days
