# P3.py
#
# Write a Python function named checkQuotes that is given a line read from a 
# text file and returns True if each quote characters in the line has a 
# matching quote (of the same type), otherwise returns False: 
#
#   ‘Today’s high temperature will be 75 degrees’ --> False
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

def checkQuotes(line):
    return not (len([*filter(lambda x: x in "\'", line)]) % 2 or \
                len([*filter(lambda x: x in "\"", line)]) % 2)

