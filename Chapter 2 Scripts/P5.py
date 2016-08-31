# P5.py
#
# this program prompts user for two integer input and display the following 
# arithmetic operations, e.g., if the user enters the values 7 and 5:
# 
#   7 + 5 = 12
#   7 - 5 = 2
#   7 * 5 = 35
#   7 / 5 = 1.40
#   7 // 5 = 1 
#   7 % 5 = 2
#   7 ** 5 = 16,807
#
# date:    08/31/2016
# author:  Chiayo Lin
# license: GPL 3.0
#

numero_uno = int(input("Enter the first number: "))
numero_dos = int(input("Enter the second number: "))

operations = lambda x, y: \
    (('+', x + y), ('-', x - y), ('*', x * y), ('/', format(x / y, '.2f')), 
      ('//', x // y), ('%', x % y), ('**', format(x ** y, ',')))

for operator, result in operations(numero_uno, numero_dos):
    print(numero_uno, operator, numero_dos, '=', result)
