# P5.py
#
# Write a Python program that prompts the user to enter a list of words 
# and stores in a list only those words whose first letter occurs again
# within the word (for example, 'Baboon'). The program should display 
# the resulting list.
#
# date:    10/31/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_list(buff):
    char = input("Enter a name: ")
    return char == '' and filter(lambda l: l[0] in l[1:], buff) or \
        get_list(buff + [char])

print(*get_list(list()), sep = ', ')
