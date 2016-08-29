# P3.py
#
# prompts user for two floating-point values, print the result of the 
# first number divided by the second number, with exactly six decimal 
# places scientific notation.
#
# date:    08/28/2016
# author:  Chiayo Lin
# license: GPL 3.0
#

dividend = int(input("Enter the first number: "))
divisor = int(input("Enter the second number: "))

print(format((dividend / divisor), '.6e'))
