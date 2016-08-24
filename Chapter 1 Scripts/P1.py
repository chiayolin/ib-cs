# P1.py 
#
# write a simple Python program that displays the following 
# powers of 2, one per line: 
#   2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7, 2^8 
# 
# usage:
#   $ python3 ./P1.py
#
# date:    08/25/2016
# author:  Chiayo Lin
# license: MIT License
#

# map a range of powers to a lambda and print them as a list
list(map(lambda x: print("2^{} =".format(x), 2**x), range(1, 9)))
