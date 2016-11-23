# P3.py
#
# Write a Python function named modCount that is given a positive integer, 
# n, and a second positive integer, m <= n, and returns how many numbers 
# between 1 and n are evenly divisible by m.
#
# date:    11/23/2016
# author:  Chiayo Lin
# license: GPL 3.0

def modCount(n, m):
    return len([*filter(lambda x: not x % m, range(1, n + 1))])
