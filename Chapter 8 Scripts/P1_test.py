# P1_test.py
#
# This file is part of P1.py.
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P1 import reduceWhitespace

for line in open("P1_text.txt", "r"): 
    print(reduceWhitespace(line))

