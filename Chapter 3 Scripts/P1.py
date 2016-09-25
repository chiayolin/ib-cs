# P1.py
#
# Write a Python program in which the user enters either 'A', 'B', or 'C'. 
# If 'A' is entered, the program should display the word 'Apple'; if 'B' 
# is entered, it displays 'Banana'; and if 'C' is entered, it displays 
# 'Coconut'. Use nested if statements for this as depicted in Figure 3-13.
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

# get input from user 
option = input("Enter A or B or C: ").lower()

# nested if is used here because the problem says so:
#   "Use nested if statements for this as depicted in Figure 3-13."
if option == 'a':
    print("Apple")
else:
    if option == 'b':
        print("Banana")
    elif option == 'c':
        print("Coconut")
    else:
        # the problem does not state what to do when the user enters an
        # invalid option so here it does nothing.
        None
