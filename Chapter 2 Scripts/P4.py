# P4.py
#
# the program prompts the user for an input and display 
# the corresponding Unicode encodings. 
#
# date:    08/28/2016
# author:  Chiayo Lin
# license: GPL 3.0
#

print(*list(map(ord, list(input("Enter a string: ")))))
