# P1.py
#
# Write a Python function called reduceWhitespace that is given a line read 
# from a text  file and returns the line with all extra whitespace characters 
# between words removed: 
#   'This line has extra space characters’ --> 
#   ‘This line has extra space characters’
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

from functools import reduce

def reduceWhitespace(line):
    
    """ 
    Returns line with extra whitespaces removed.
    """

    return reduce(lambda h, t: h + ' ' + t, line.split()).strip()

