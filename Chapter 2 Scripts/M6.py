# M6.py
#
# Modify the Age in Seconds program so that it determines the difference in 
# age in seconds of two friends.
#
# date:    09/09/2016
# author:  Charles Dierbach, Chiayo Lin
# license: n/a 

# Age in Seconds Program
# This program will calculate a person's approximate in seconds

import datetime

# Program Greeting
print('This program computes the approxamte difference in age in', 
      'seconds of two people based on a provided date of birth.',
      'Only ages for dates of birth starting from can be compute.', sep = '\n')

# get month, day, year of birth
print("\nEnter birthday for the first user...")
u1_month_birth = int(input('Enter month born (1-12): '))
u1_day_birth = int(input ('Enter day born (1-31): '))
u1_year_birth = int(input('Enter year born (4-digit): '))

print("\nEnter birthday for the second user...")
u2_month_birth = int(input('Enter month born (1-12): '))
u2_day_birth = int(input ('Enter day born (1-31): '))
u2_year_birth = int(input('Enter year born (4-digit): '))

# get current month, day, year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

# determine number of seconds in a day, average month and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

def age_in_seconds(month_birth, day_birth, year_birth):
    # calculate approximate age in seconds
    numsecs_1900_dob = (year_birth - 1900) * avg_numsecs_year + \
        (month_birth - 1) * avg_numsecs_month + \
            (day_birth * numsecs_day)
    numsecs_1900_today = (current_year - 1900) * avg_numsecs_year + \
        (current_month - 1) * avg_numsecs_month + \
            (current_day * numsecs_day)

    return numsecs_1900_today - numsecs_1900_dob

age_difference_in_seconds = \
    age_in_seconds(u1_month_birth, u1_day_birth, u1_year_birth) - \
        age_in_seconds(u2_month_birth, u2_day_birth, u2_year_birth)

# output results
print('\nThe differnce in age between two users is about',
      abs(age_difference_in_seconds), 'seconds.')
