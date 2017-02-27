# P3.py
#
# Write a Python function named getDailyTemps that prompts the user for the 
# average temperature for each day of the week, and returns a dictionary 
# containing the entered information.
#
# date:    02/27/2017
# author:  Chiayo Lin
# license: GPL 3.0

def getDailyTemps():
    temp = {}
    week = ("mon", "tue", "wed", "thu", "fri", "sat")
    for day in week:
        temp[day] = float(input("Temperature for " + day.upper() + ": "))

    return temp
