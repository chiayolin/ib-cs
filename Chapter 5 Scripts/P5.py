# P5.py
#
# Write a Python function named printAsterisks that is passed a positive 
# integer value n, and prints out a line of n asterisks. If n is greater 
# than 75, then only 75 asterisks should be displayed.
#
# date:    11/23/2016
# author:  Chiayo Lin
# license: GPL 3.0

def printAsterisks(n):
    print(not n and '\n' or '*', end = '')

    return n != 0 and printAsterisks((n > 75 and 75 or n) - 1)
