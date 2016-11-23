# P1.py
#
# Write a Python function named zeroCheck that is given three integers, 
# and returns true if any of the integers is 0, otherwise it returns false.
#
# date:    11/23/2016
# author:  Chiayo Lin
# license: GPL 3.0

def zeroCheck(x, y, z):
    return not (x and y and z)
