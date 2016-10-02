# P7.py
#
# Display the integer values 1–100 as given in question P6 using 
# only one while loop.
#
# date:    10/02/2016
# author:  Chiayo Lin
# license: GPL 3.0

counter = 0
while counter != 100:
    counter += 1
    print(format(counter, "4d"), end = '')
    not counter % 10 and print() or None
