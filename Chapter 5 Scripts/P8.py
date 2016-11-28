# P8.py
#
# Implement the Python function described in question P7 so that the altered
# list is returned as a function value, rather than by side effect.
#
# date:    11/28/2016
# author:  Chiayo Lin
# license: GPL 3.0

def levelThreshold(lst, threshold):
    return [*map(lambda x: 0 if x > threshold else x, lst))]
