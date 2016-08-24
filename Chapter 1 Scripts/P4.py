# P4.py 
#
# write a Python program that allows the user to enter a four
# -digit _input number and displays its value in base 10. each 
# _input digit should be entered one per line, starting with 
# the leftmost digit , as shown below:
#
# Enter leftmost digit: 1
# Enter the next digit: 0
# Enter the next digit: 0
# Enter the next digit: 1
# The value is 9
#
# date:    08/25/2016
# author:  Chiayo Lin
# license: MIT License
#

_range = 4
_input = [0] * _range
_tuple = zip(range(0, _range), list(reversed(range(_range))))

prompt = ("leftmost", "the next")
for place, power in _tuple:
    print("Enter", prompt[1 if place else 0], "digit: ", end = '')
    _input[place] = int(input()) * (2**power)

print("The value is", sum(_input))
