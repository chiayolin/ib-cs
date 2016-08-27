# P2.py 
#
# write a Python program that allows the user to enter any integer va-
# lue, and displays the value of 2 raised to that power. Your program 
# should function as shown below:
#
#   what power of 2? 10
#   2 to the power of 10 is 1024
#
# date:    08/25/2016
# author:  Chiayo Lin
# license: MIT License
#

# λeah
(lambda x: print("2 to the power of", x, "is", 2**x))(\
    int(input("What power of 2? ")))
