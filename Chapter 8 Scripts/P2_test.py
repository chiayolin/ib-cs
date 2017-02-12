# P2_test.py
#
# This file is part of P2.py.
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P2 import extractTemp

for line in open("P2_text.txt", "r"):
    print(extractTemp(line))
