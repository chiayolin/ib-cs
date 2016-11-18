# P4.py
#
# Write a Python program that prompts the user to enter a list of first 
# names and stores them in a list. The program should display how many 
# times the letter 'a' appears within the list.
#
# date:    10/31/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_list(freq):
    char = input("Enter a first name: ")
    return char == '' and freq or \
           get_list(freq + len([*filter(lambda c: c is 'a', char)]))

print("The letter 'a' appears", get_list(0), "times in the list.")
