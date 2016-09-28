# P4.py
#
# Write a program that sums a series of (positive) integers entered by the 
# user, excluding all terms that are greater than 100.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

print("Numbers greater than 100 will be excluded.")

series = term = 0
while term >= 0:
    term = int(input("Enter an integer (-1 to end): "))
    series += term <= 100 and term >= 0 and term
print("The sum of the sequence is ", series, '.', sep = '')
