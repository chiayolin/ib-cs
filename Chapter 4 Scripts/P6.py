# P6.py
#
# Write a Python program that prompts the user to enter types of fruit, 
# and how many pounds of fruit there are for each type. The program 
# should then display the information in the form fruit, weight listed 
# in alphabetical order, one fruit type per line as shown below,
#
#   Apple, 6 lbs.
#   Banana, 11 lbs.
#   (etc.)
#
# date:    10/31/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_list(buff):
    fruit = input("Enter a fruit name: ")
    weight = input("Enter its weight (lbs): ")

    return (fruit == '' or weight == '') and             \
        sorted(buff) or get_list(buff + [[fruit, weight]])

fruit_info = get_list(list()); print(end = '\n')
list(map(lambda x: print(x[0] + ',', x[1], 'lbs.'), fruit_info))
