# P3.py
#
# Write a Python program that prompts the user for a list of integers and 
# stores them in a list.Forallvalues that are greater than 100, the 
# string 'over' should be stored instead. The program should display the 
# resulting list.
#
# date:    10/31/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_list(buff):
    char = input("Enter an integer: ")
    return char == '' and buff or \
        get_list(buff + (int(char) < 100 and [char] or ['over']))

print(*get_list(list()), sep = ', ')
