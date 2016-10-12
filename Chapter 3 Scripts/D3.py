# D3.py - The First-Time Home Buyer Tax Credit
#
# Develop and test a Python program that determines if an individual qualifies 
# for a government First-Time Home Buyer Tax Credit of $8,000. The credit was 
# only available to those that (a) bought a house that cost less than $800,000, 
# (b) had a combined income of under $225,000 and (c) had not owned a primary 
# residence in the last three years.
#
# date:    10/12/2016
# author:  Chiayo Lin
# license: GPL 3.0

print('''This program is designed to determine if a person is qualify 
for a government First-Time Home Buyer Tax Credit of $8,000. 
Please answer the following questions truthfully:\n''')

gets = lambda s: input(s + " (y/n)? ").split()[0].lower() == 'y' and 1 or 0

cond_A = gets("Have you bought a house that cost less than $800,000")
cond_B = gets("Do you have a combined income under $225,000")
cond_C = gets("Have you not owned a primary residence in the last 3 years")

print("\nYes. You are qualified.") if cond_A and cond_B and cond_C else \
    print("\nSorry. You are not qualified.")
