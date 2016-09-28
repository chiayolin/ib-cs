# P5.py
#
# Write a program, in which the user can enter any number of positive and
# negative integer values, that displays the number of positive values 
# entered, as well as the number of negative values.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

term = None
sequence = []
while term is not 0:
    term = int(input("Enter an integer (0 to end): "))
    term is not 0 and sequence.append(term)

positive = list(filter(lambda term: term > 0, sequence))
negative = list(filter(lambda term: term < 0, sequence))

print(len(positive), len(negative), sep = '\n')
