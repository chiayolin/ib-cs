# P4.py
#
# prompts the user for an input and display the corresponding Unicode encodings. 
#
# date:    08/28/2016
# author:  Chiayo Lin
# license: GPL 3.0
#

print(*list(map(lambda x: ord(x), 
    list(input("Enter a string: ")))))
