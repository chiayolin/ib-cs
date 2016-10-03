# M7.py - Coin Change Exercise Program: Raising the Challenge
# 
# Modify the Coin Change Exercise program in section 3.4.6 so that the least 
# possible number of coins must be entered. For example, the least number of
# coins that total to 43 cents is 6 (one quarter, one dime, one nickel, and 
# three pennies).
# 
# date:    10/03/2016
# author:  n/a
# license: n/a

# Coin Change Exercise Program

import random

# program greeting
print('The purpose of this exercise is to enter a number of coin values')
print('that add up to a displayed target value.\n')
print('Enter coins values as 1: penny, 5: nickel, 10: dime, 25: quarter' + 
      ' and 50: half-dollar')
print("Hit return after the last entered coin value.")
print('----------------')

# init
terminate = False
empty_str = ''
coin_amnt = 0

# start game
while not terminate:
    amount = random.randint(1,99)

    # bad implementation for a greedy algorithm, good enough for now.
    # to get the least possible number of coins for the given amount:
    coin_total = 0
    amount_tot = amount 
    for coin_val in (50, 25, 10, 5, 1):
        if amount_tot // coin_val != 0:
            coin_total += amount_tot // coin_val
            amount_tot -= coin_val * (amount_tot // coin_val)
    
    print('Enter coins that add up to', amount, 'cents, one per line.\n')
    total = coin_counter = 0
    game_over = False

    while not game_over:
        valid_entry = False
        
        while not valid_entry:
            if total == 0:
                entry = input('Enter first coin: ')
            else:
                entry = input('Enter next coin: ')
                
            if entry in (empty_str,'1','5','10','25', '50'):
                valid_entry = True
            else:
                print('Invalid entry')
        
        if entry == empty_str:
            if total == amount:
                print('Correct!')
            else:
                print('Sorry - you only entered', total, 'cents.')
                
            game_over = True
            
        else:
            coin_counter += 1  # increment the coin counter
            total += int(entry)
            if total > amount:
                print('Sorry - total amount exceeds', amount, 'cents.')
                game_over = True
            # break the iteration if coin counter exceeds the least possible
            # number of coins:
            elif coin_counter > coin_total:
                print('Sorry - least possible number of coins must be entered')
                game_over = True
                
        if game_over:
            entry = input('\nTry again (y/n)?: ')
            
            if entry == 'n':
                terminate = True

print('Thanks for playing ... goodbye')
