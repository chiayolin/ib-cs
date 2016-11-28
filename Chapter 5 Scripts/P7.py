# P7.py
#
# Implement a Python function that is passed a list of numeric values and 
# a particular threshold value, and returns the list with all values above 
# the given threshold value set to 0. The list should be altered as a side 
# effect to the function call, and not by function return value.
#
# date:    11/28/2016
# author:  Chiayo Lin
# license: GPL 3.0

def above_max_to_zero(lst, threshold):
    lst_buff = enumerate(map(lambda x: 0 if x > threshold else x, lst))
    for index, value in lst_buff:
        lst[index] = value

    return None
