# M1.py - Chinese Zodiac Program: Japanese and Vietnamese Variations
#
# Modify the Chinese Zodiac program in the chapter to allow the user 
# to select the Chinese Zodiac, the Japanese Zodiac, or the Vietnamese 
# Zodiac. The Japanese Zodiac is the same as the Chinese Zodiac, except 
# that “Pig” is substituted with “Wild Boar.” The Vietnamese Zodiac is 
# also the same except that the “Ox” is substituted with “Water Buffalo” 
# and “Rabbit” is replaced with “Cat.”
#
# date:    09/25/2016
# author:  Chiayo Lin
# license: GPL 3.0

# Chinese Zodiac Program

import datetime

# init
zodiac_animals = ('Rat', ('Ox', 'Water Buffalo'), 'Tiger', ('Rabbit', 'Cat'), 
                  'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 
                  'Dog', ('Pig', 'Wild Boar'))

rat = 'Forthright, industrious, sensitive, intellectual, sociable'
ox = 'Dependable, methodical, modest, born leader, patient'
tiger = 'Unpredictable, rebellious, passionate, daring, impulsive'
rabbit = 'Good friend, kind, soft-spoken, cautious, artistic'
dragon = 'Strong, self-assured, proud, decisive, loyal'
snake = 'Deep thinker, creative, responsible, calm, purposeful'
horse = 'Cheerful, quick-witted, perceptive, talkative, open-minded'
goat = 'Sincere, sympathetic, shy, generous, mothering'
monkey = 'Motivator, inquisitive, flexible, innovative, problem solver'
rooster = 'Organized, self-assured, decisive, perfectionist, zealous'
dog = 'Honest, unpretentious, idealistic, moralistic, easy going'
pig = 'Peace-loving, hard-working, trusting, understanding, thoughtful'

characteristics = (rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey,
                   rooster, dog, pig)

terminate = False

# program greeting
print('This program will display your Chinese/Japanese/Vietnamese')
print('zodiac sign and associated personal characteristics.\n')

# get current year from module datetime
current_yr = datetime.date.today().year

while not terminate:
    ethnicity = \
        input('Choose a subset of Chinese zodiac sign (ZH/JP/VN): ').lower()[0]

    # get year of birth
    birth_year = int(input('Enter your year of birth (yyyy): '))
    
    while birth_year < 1900 or birth_year > current_yr:
        print('Invalid year. Please re-enter\n')
        birth_year = int(input('Enter your year of birth (yyyy): '))

    # output results
    cycle_num = (birth_year - 1900) % 12
    
    print('\nYour',                                                               \
        ethnicity == 'v' and 'Vietnamese' or                                      \
        ethnicity == 'j' and 'Japanese' or 'Chinese', 'zodiac sign is',           \
        (type(zodiac_animals[cycle_num]) is tuple and (ethnicity in ('j', 'v') and \
              zodiac_animals[cycle_num][1] or                                       \
              zodiac_animals[cycle_num][0]) or                                      \
              zodiac_animals[cycle_num]) + '.\n')

    print('Your personal characteristics ...')
    print(characteristics[cycle_num])

    # continue?
    response = input('\nWould you like to enter another year? (y/n): ')
    
    while response != 'y' and response != 'n':
        response = input("Please enter 'y' or 'n': ")

    if response == 'n':
        terminate = True
