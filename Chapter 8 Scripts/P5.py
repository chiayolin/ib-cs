# P5.py
#
# Write a Python function list_d interleaveChars that is given two names 
# read from a text  file, and returns a single result containing the 
# characters of each result interleaved:
#
#       'Hello', 'Goodbye' --> 'HGeololdobye'
#
# date:    02/17/2017
# author:  Chiayo Lin
# license: GPL 3.0

def interleaveChars(list_1, list_2):
    shortest, longest = len(list_1) > len(list_2) and      \
                        (list_2, list_1) or (list_1, list_2)

    index = 0
    result = ''
    while index != len(shortest):
        result += list_1[index] + list_2[index]
        index += 1
    result += longest[len(shortest):]
    
    return result

