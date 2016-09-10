# M2.py
#
# Modify the Restaurant Tab Calculation program of section 2.2.5 so that, in
# addition to displaying the total of the items ordered, it also displays the 
# total amount spent on drinks and dessert, as well as the percentage of the 
# total cost of the meal (before tax) that these items comprise. Display the 
# monetary amount rounded to two decimal places.
#
# date:    09/09/2016
# author:  Charles Dierbach, Chiayo Lin
# license: n/a 

# Restaurant Tab Calculation Program
# This program will calculate a restaurant tab with a gift certificate

# initialization
tax = 0.08

# program greeting
print('This program will calculate a restaurant tab for a couple with')
print('a gift certificate, with a restaurant tax of', tax * 100, '%\n')

# get amount of gift certificate
amt_certificate = float(input('Enter amount of the gift certificate: '))

# cost of ordered items
print('Enter ordered items for person 1')

appetizer_per1 = float(input('Appetizier: '))
entree_per1 = float(input('Entree: '))
drinks_per1 = float(input('Drinks: '))
dessert_per1 = float(input('Dessert: '))

print('\nEnter ordered items for person 2')

appetizer_per2 = float(input('Appetizier: '))
entree_per2 = float(input('Entree: '))
drinks_per2 = float(input('Drinks: '))
dessert_per2 = float(input('Dessert: '))

# total items
amt_person1 = appetizer_per1 + entree_per1 + drinks_per1 + dessert_per1
amt_person2 = appetizer_per2 + entree_per2 + drinks_per2 + dessert_per2

# compute tab with tax
items_cost = amt_person1 + amt_person2
tab = items_cost + items_cost * tax

# total drinks and dessert
drinks_and_dessert_total = \
    drinks_per1 + drinks_per2 + dessert_per1 + dessert_per2
drinks_and_dessert_percentage = drinks_and_dessert_total / items_cost

# display amount owe
print('\nOrdered items: $', format(items_cost, '.2f'))
print('The amount spend on drinks and dessert is', 
    format(drinks_and_dessert_total, '.2f'))
print('Drinks and dessert composed', 
    format(drinks_and_dessert_percentage, '.2f') + '%', 'of the total cost')
print('Restaurant tax: $', format(items_cost * tax, '.2f'))
print('Tab: $', format(tab - amt_certificate, '.2f'))
print('(negative amount indicates unused amount of gift certificate)')
