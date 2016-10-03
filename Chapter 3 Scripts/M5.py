# M5.py - Oil Change Noti cation Program: Number of Miles before Change
# 
# Modify the Oil Change Noti cation program in Figure 3-21 so that the program 
# displays the number of miles left before the next oil change, or the number 
# of miles overdue for an oil change, as appropriate.
#
# date:    10/03/2016
# author:  n/a
# license: n/a

# display program welcome
print('This program will determine if your car is in need of an oil change')

# init
miles_between_oil_change = 7500  # num miles between oil changes
miles_warning = 500      # how soon to warn of needed oil change
valid_entries = False

# get mileage of last oil change and current mileage and display
while not valid_entries:
    mileage_last_oilchange = int(input('Enter mileage of last oil change: '))
    current_mileage = int(input('Enter current mileage: '))

    if current_mileage - mileage_last_oilchange < 0:
             print('Invalid entry – current mileage entered is less than')
             print('mileage entered of last oil change')
    else:
        miles_traveled = current_mileage - mileage_last_oilchange
        valid_entries = True
        
if miles_traveled >= miles_between_oil_change:
    print(str(miles_traveled - miles_between_oil_change) + 
        ' miles overdue.\nYou are due for an oil change')
elif miles_traveled >= miles_between_oil_change - miles_warning:
    print(str(miles_between_oil_change - miles_traveled) + 
        ' miles left before the next oil change.\n' +
        'You will soon be due for an oil change.')
else:
    print('You are not in immediate need of an oil change')

