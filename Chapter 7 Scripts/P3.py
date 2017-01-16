# P3.py
#
# Implement a set of functions called getData, extractValues, and calcRatios. 
# Function getData should prompt the user to enter pairs of integers, two per 
# line, with each pair read as a single string, for example,
#
#   Enter integer pair (hit Enter to quit): 134 289 (read as '134 289')
#   etc.
#
# These strings should be passed one at a time as they are being read to 
# function extractValue, which is designed to return the string as a tuple of 
# two integer values,
#
#   extractValues('134 289') returns (134, 289) etc.
#
# Finally, each of these tuples is passed to function calcRatios one at a time 
# to calculate and return the ratio of the two values. For example,
#
#   calcRatios((134, 289)) returns 0.46366782006920415 etc.
#
# Implement a complete program that displays a list of ratios for an entered series 
# of integer value pairs. Make sure to include docstring specification for each of 
# the functions.
#
# date:    01/16/2017
# author:  Chiayo Lin
# license: GPL 3.0

def getData(buff = []):
    
    """
    getData prompts the user to enter pairs of integers, two per line, with 
    each pair read as a single string:

        Enter integer pair (hit Enter to quit): 1 2
        Enter integer pair (hit Enter to quit): 5 3
    
    For the example above the function returns [['1', '2'], ['5', 3']]
    """

    pair = input("Enter integer pair (hit Enter to quit): ")
    return pair == '' and buff or getData([pair] + buff)

def extractValues(values, buff = [], counter = 0):
    
    """
    extractValues takes a list of strings and returns a list of pairs in
    the atomic values of each integer in the string:
    
        ('1', '2'), ('3', '4')) --> ((1, 2), (3, 4))
    """
    
    return counter != len(values) - 1 and buff or extractValues(values, \
           [[*map(int, values[counter].split(" "))]] + buff, counter + 1)

def calcRations(pairs):
    
    """
    calcRations takes a list of pairs and returns the quotient of the head
    divided by the tail of each pair in a list.
    """
    
    return [*map(lambda x: x[0] / x[1], pairs)]

def main():
    
    """
    The complete implementation of the program
    """

    print(*calcRations(extractValues(getData())), sep = '\n')

    return

