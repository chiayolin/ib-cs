# M1.py - Temperature Conversion Program: Input Error Checking
#
# Modify the Temperature Conversion program in Figure 3-19 to perform 
# input error checking of entered temperatures. On the Fahrenheit scale, 
# absolute zero is 2459.67. Therefore, all valid Fahrenheit temperatures 
# start at that value (with no upper limit). On the Celsius scale, 
# absolute zero is 2273.15. The program should reprompt the user for any 
# invalid entered temperatures.
# 
# date:    10/02/2016
# author:  n/a
# license: n/a

# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')

while which != 'F' and which != 'C':
    which = input("Please enter 'F' or 'C': ")

temp = float(input('Enter temperature to convert: '))
while temp < { 'F' : -459.67, 'C' : -273.15 }[which]:
    temp = float(input("Invalid, try again: "))

# Determine temperature conversion needed and display results
if which == 'F':
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
