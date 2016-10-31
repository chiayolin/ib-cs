# P1.py
#
# write a Python program that prompts the user for a list of integers, 
# stores in another list only those values between 1–100, and displays 
# the resulting list.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_integer_list(buff):
    char = input("Enter an integer: ")
    return char == '' and                                  \
        filter(lambda n: int(n) in range(1, 101), buff) or \
        get_integer_list(buff + [char])

filtered_integers = get_integer_list(list())
print("Values entered between 1-100 are: ", end = '')
print(*filtered_integers, sep = ', ')
