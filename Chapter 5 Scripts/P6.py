# P6.py
#
# Writea Python function named getContinue that displays to the user “Do 
# you want to continue (y/n): ”, and continues to prompt the user until 
# either uppercase or lowercase 'y' or 'n' is entered, returning 
# (lowercase) 'y' or 'n' as the function value.
#
# date:    11/23/2016
# author:  Chiayo Lin
# license: GPL 3.0

def getContinue():
    result = input("Do you want to continue (y/n): ").lower()
    if result != '' and result[0] in ('y', 'n'):
        return result[0]

    return getContinue()
