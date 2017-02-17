# P5_test.py
#
# This file is part of P5.py.
#
# date:    02/17/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P5 import interleaveChars

index = 0
test_file = list(open("P5_text.txt", 'r'))
while index != len(test_file):
    line_1 = test_file[index][:-1]
    line_2 = test_file[index + 1][:-1]
    print(line_1, line_2, interleaveChars(line_1, line_2), 
          sep = '\n', end = '\n\n')

    index += 2

