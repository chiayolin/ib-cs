# P3.py
#
# Write a Python program in which a student enters the number of college credits 
# earned. If the number of credits is greater than 90, 'Senior Status' is 
# displayed; if greater than 60, 'Junior Status' is displayed; if greater than 
# 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

# get input from user 
credits = int(input("Enter credits earned: "))
level = credits > 90 and "Senior" or \
        credits > 60 and "Junior" or \
        credits > 30 and "Sophomore" or "Freshman"
print(level, "Status")
