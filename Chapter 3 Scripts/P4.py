# P4.py
#
# Write a program that sums a series of (positive) integers entered by the 
# user, excluding all numbers that are greater than 100.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

# "functional" style so no loops are used.

# print instruction for the user
print("Enter a list of numbers, separate by commas,",
      "numbers greater than 100 will be excluded:", sep = '\n')

# get a list of integers and remove non-digits, commas, and whitespaces
str_to_int = lambda term: term.strip().isdigit() and int(term)
sequence = list(map(str_to_int, input(">>> ").split(',')))

# filter out numbers greater than 100, sum the rest, and print the result
series = sum(list(filter(lambda term: term < 100, sequence)))
print("The sum of the sequence you entered is ", series, '.', sep = '')
