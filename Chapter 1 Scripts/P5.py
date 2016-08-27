# P5.py 
# 
# Write a simple Python program that prompts the user for a certain 
# number of cities for the Traveling Salesman problem, and displays 
# the total number of possible routes that can be taken. Your prog-
# ram should function as shown below:
# 
#   How many cities? 10
#   For 10 cities, there are 3628800 possible routes
#
# date:    08/25/2016
# author:  Chiayo Lin
# license: MIT License
#

import math

(lambda n: print("For {} cities, there are {} possible routes".
    format(n, math.factorial(n))))(int(input("How many cities? ")))
