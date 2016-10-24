# D2.py - Leap Years to Come
#
# Develop and test a Python program that displays future leap years, starting 
# with the  rst occurring leap year from the current year, until a final year 
# entered by the user. (HINT: Module datetime used in the Age in Seconds 
# Program of Chapter 2 will be needed here.)
#
# date:    10/11/2016
# author:  Chiayo Lin
# license: GPL 3.0

import datetime

is_leap_year = lambda y: \
    (y % 4 and -1 or y % 100 and 1 or y % 400 and -1 or 1) > 0

def next_leap_year(now):
    if is_leap_year(now):
        return now
    return next_leap_year(now + 1)

now = datetime.datetime.now().year
end = int(input("Ente a final year: "))
print(*filter(is_leap_year, range(next_leap_year(now), end + 4, 4)), sep = '\n')


'''
Chiayo, this program has a logic error. 2100, 2200 and 2300 ar not
leap years. 2400 is.

It's difficult to follow the logic with magic numbers like -1 and 1
that are on line 15, but I'm pretty sure the error is the order of
operations.
'''
