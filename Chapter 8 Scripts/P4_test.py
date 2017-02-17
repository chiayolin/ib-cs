# P4_test.py
#
# This file is part of P4.py.
#
# date:    02/14/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P4 import countAllLetters

for line in open("P4_text.txt", 'r'):
    print(line[:-1] + " --->\n", countAllLetters(line))

