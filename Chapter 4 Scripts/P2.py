# P2.py
#
# Write a Python program that prompts the user for a list of integers, 
# stores in another list only those values that are in tuple valid_values, 
# and displays the resulting list.
#
# date:    10/28/2016
# author:  Chiayo Lin
# license: GPL 3.0

valid_values = (1, 2, 4, 8, 16, 32)

def get_integer_list(buff):
    char = input("Enter an integer: ")
    return char == '' and                                    \
           filter(lambda n: int(n) in valid_values, buff) or \
           get_integer_list(buff + [char])

print("Only these values will be stored:", valid_values)
filtered_integers = get_integer_list(list())
print("Valid values entered are: ", end = '')
print(*filtered_integers, sep = ', ')
