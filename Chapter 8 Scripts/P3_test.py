# P3_test.py
#
# This file is part of P3.py.
#
# date:    02/12/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P3 import checkQuotes

for line in open("P3_text.txt", 'r'):
    print(format(line.strip(), "<26"), "-->", checkQuotes(line))
