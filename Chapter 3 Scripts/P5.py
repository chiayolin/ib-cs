# P5.py
#
# Write a program, in which the user can enter any number of positive and
# negative integer values, that displays the number of positive values 
# entered, as well as the number of negative values.
#
# date:    09/26/2016
# author:  Chiayo Lin
# license: GPL 3.0

import sys

print("This program counts the number of +/- values are entered.")

term = None
positive = negative = 0
while term != 0:
    try:
        term = int(input("Enter an integer (0 to end): "))
    except (ValueError, TypeError):
        print("Error: illegal charecter(s)", file = sys.stderr)
        pass
    else:
        positive += term != 0 and term > 0 and 1
        negative += term != 0 and term < 0 and 1

pluralise = lambda number: number < 2 and "value" or "values"
print("There are {} positive {} and {} negative {}.".
    format(positive, pluralise(positive), negative, pluralise(negative)))
