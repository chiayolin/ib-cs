# P2.py
#
# Repeat question P1 using an if statement with elif headers instead.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

# get input from user 
option = input("Enter A or B or C: ").lower()

if option == 'a':
    print("Apple")
elif option == 'b':
        print("Banana")
elif option == 'c':
        print("Coconut")
else:
    # the problem does not state what to do when the user enters an
    # invalid option so here it does nothing.
    None
