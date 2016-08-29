# P1.py
#
# alternative version:
#   https://gist.github.com/chiayolin/f2ea88579a253edbb65c71c4236bef4c
#
# prompts user for two interger values, print the result of the first number 
# divided by the second number, with exactly two decimal places.
#
# date:    08/28/2016
# author:  Chiayo Lin
# license: GPL 3.0
#

dividend = int(input("Enter the first number: "))
divisor = int(input("Enter the second number: "))

print(format((dividend / divisor), '.2f'))
