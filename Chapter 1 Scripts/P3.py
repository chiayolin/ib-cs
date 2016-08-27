# P3.py 
# 
# write a Python program that allows the user to enter any integer 
# base and integer exponent, and displays the value of the base 
# raised to that exponent. your program should function as shown 
# below:
#
#   what base? 10
#   what power of 10? 4
#   10 to the power of 4 is 10000
#
# date:    08/25/2016
# author:  Chiayo Lin
# license: MIT License
#

# "self-documenting code"
what = ["here stores the base", "the power stores here"]
for now, prompt in enumerate(("What base? ", "What power of {}? ")):
    print(prompt.format(what[now - 1]), end = '')
    what[now] = int(input())

(lambda base, power: print("{} to the power of {} is {}".
    format(base, power, base**power)))(what[0], what[1])
