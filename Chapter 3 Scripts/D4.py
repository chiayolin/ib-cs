# D4.py - Home Loan Amortization
#
# Develop and test a Python program that calculates the monthly mortgage 
# payments for a given loan amount, term (number of years) and range of 
# interest rates from 3% to 18%. The fundamental formula for determining 
# this is A / D, where A is the original loan amount, and D is the 
# discount factor. The discount factor is calculated as,
#
#   D = ((1 + r)^n - 1) / r(1 + r)^n
#
# where n is the number of total payments (12 times the number of years of 
# the loan) and r is the interest rate, expressed in decimal form (e.g., .05), 
# divided by 12. A monthly payment table should be generated as shown below,
#
# Loan Amount: $350,000 Term: 30 years
# Interest Rate        Monthly Payment
#      3%                  1475.61
#      4%                  1670.95
#      5%                  1878.88
#      6%                  2098.43
#      .                   .
#      .                   .
#      18%                 5274.80
#
# date:    10/11/2016
# author:  Chiayo Lin
# license: GPL 3.0

term = int(input("Enter the term: "))
start_rate = 3
final_rate = 18
amount = int(input("Enter the amount: "))


discount_factor = lambda r, n: ((1 + r) ** (n) - 1) / (r * (1 + r) ** n)

def print_rate_table(rate):
    print("     {0:<21}{1:.2f}".format(str(rate) + '%', 
        amount / discount_factor(rate / 100 / 12, term * 12)))
    
    if rate == final_rate: 
        return None
    return print_rate_table(rate + 1)

print("Loan Amount: ${0:,}  Term: {1} years".format(amount, term))
print("Interest Rate         Monthly Payment")
print_rate_table(start_rate)

'''
This program should ask the user for an amount and number of years.
Even better would be to ask for the rates as well.
'''
