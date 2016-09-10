# M4.py
#
# modify the Temperature Concersion program in section 2.4.6 to convert 
# from Celsius to Fahrenheit instead. The formula for the conversion is
# f = (c * (9 / 5)) + 32
#
# date:    09/09/2016
# author:  Charles Dierbach, Chiayo Lin
# license: n/a

# Temperature Conversion Program (Celsius to Fahrenheit)

# This program will convert a temperature entered in Celsius
# to the equivalent degrees in Fahrenheit

# program greeting
print('This program will convert degrees Celsius to degrees Fahrenheit')

# get temperature in Fahrenheit
celsius = float(input('Enter degrees Celsius: '))

# calc degrees Fahrenheit
fahrenheit = (celsius * (9 / 5)) + 32

# output degrees Celsius
print(celsius, 'degrees Celsius equals',
    format(fahrenheit, '.1f'), 'degrees Fahrenheit')
