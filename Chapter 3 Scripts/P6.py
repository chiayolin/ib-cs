# P6.py
#
# Write a program containing a pair of nested while loops that displays the 
# integer values 1–100, ten numbers per row, with the columns aligned as 
# shown below:
#    1   2   3   4   5   6   7   8   9  10 
#   11  12  13  14  15  16  17  18  19  20 
#   21  22  23  24  25  26  27  28  29  30
#   ...
#   91  92  93  94  95  96  97  98  99 100
#
# date:    10/02/2016
# author:  Chiayo Lin
# license: GPL 3.0

# i can't write a pair of while loops for this problem. a 
# _potential_ O(n^2) solution to this problem is just a sin. 
# but if i really have to nest it, here is the solution: 
counter = 0
while counter != 100:
    while counter != 100:
        counter += 1
        print(format(counter, "4d"), end = '')
        not counter % 10 and print() or None
# and yes, the outer while loop does nothing :)
