# D5.py - Life Signs
#
# PROBLEM:
# Develop and test a program that determines how many breaths and how many 
# heartbeats a person has had in their life. The average respiration 
# (breath) rate of people varies with age. Use the breath rates given below
# for use in your program:
#
#   +---------------+-------------------+
#   |     Age       | Breath per Minute |
#   +---------------+-------------------+
#   | Infant (0)    |      25 - 60      |
#   | 1 - 4 years   |      20 - 30      |
#   | 5 - 14 years  |      15 - 25      |
#   | 15 - 18 years |      11 - 23      |
#   +---------------+-------------------+
# 
# For heart rate, use an average of 67.5 beats per minute.
#
# SOLUTION:
# Write a program that prompts the user for an age between 0 to 18 and 
# prints out the total heartbeats and breathes taken. Futhermore, the 
# amount of breath taken is determined using the average of breath per
# minute:
#
#   +---------------+------------------+
#   |     Age       |  Average B.P.Y.  |
#   +---------------+------------------+
#   | Infant (0)    |     22338000     |
#   | 1 - 4 years   |     13140000     |
#   | 5 - 14 years  |     10512000     |
#   | 15 - 18 years |     8935200      |
#   +---------------+------------------+
#
# date:    10/14/2016
# author:  Chiayo Lin
# license: GPL 3.0

def heartbeats(age):
    # 6.75 * 365 * 24 * 60 --> 212868000
    # age + 1 because infant year is taken into the account.
    return 212868000 * (age + 1)

def respiration(age):
    # because Python's lambda is broken, "and" & "or" are used here
    # to emulate the behavior of a regular if-elif-else statement.
    # here's an interesting article to read:
    #   <http://xahlee.info/perl-python/python_3000.html>
    avg_breath_per_year_by_age = lambda y:  \
        y <=  0 and 22338000 or             \
        y >=  1 and y <=  4 and 13140000 or \
        y >=  5 and y <= 14 and 10512000 or \
        y >= 15 and y <= 18 and 8935200
    
    # create a list of integers from 0 to age + 1, map that list to 
    # a lambda that takes an age and returns the corresponding
    # breathes taken in that year. Finally, find the sum of the 
    # resulting list and return the sum (total breaths taken).
    return sum(map(avg_breath_per_year_by_age, range(0, age + 1)))

# below is an example of the code that gives people nightmares but we 
# are not mutating any varibles (yay!) since int(input(...)) is taken 
# as the function arguement to a lambda.
(lambda age: print("Invalid input.") if age not in range(0, 18 + 1) \
    else print("You have had", heartbeats(age), "heartbeats",       \
        "and you have taken", respiration(age), "breaths."))        \
            (int(input("What is your age (0 - 18)? ")))
