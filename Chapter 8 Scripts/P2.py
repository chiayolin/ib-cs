# P2.py
#
# Write a Python function named extractTemp that is given a line read 
# from a text file and displays the one number (integer) found in the string:
#
#   ‘The high today will be 75 degrees’ ---> 75
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

def extractTemp(line):
    result = [*filter(lambda x: x.isdigit(), line.split())]

    return result and result[0] or ''

