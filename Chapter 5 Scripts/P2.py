# P2.py
#
# Write a Python function named ordered3 that is passed three 
# integers, and returns true if the three integers are in order 
# from smallest to largest, otherwise it returns false.
#
# date:    11/23/2016
# author:  Chiayo Lin
# license: GPL 3.0

def ordered3(x, y, z):
    return x <= y and y <= z
