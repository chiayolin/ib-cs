# M3.py
#
# modify the Your Place in the Universe program in section 2.2.3 for
# international users, so that the user enters their weight in kilograms,
# and not in pounds.
#
# author:  n/a
# date:    n/a
# license: n/a
#
# Your Place in the Universe Program
#
# This program will determine the approximate number of atoms that a person is
# person consists of and the percent of the universe that they comprise
#

# Initialization
num_atoms_universe = 10e80
weight_avg_person = 70  # 70 kg (154 lbs)
num_atoms_avg_person = 7e27

# Program greeting
print('This program will determine your place in the universe.')

# Prompt for user's weight
weight_kg = int(input('Enter your weight in kilograms: '))

# I think the expression below is wrong because 1 kg is equal to 2.2 lbs,
# so if you want to convert to kg from lbs, instead mutiplying it by 2.2.  
# you should divide lbs by 2.2. For now I will just keep this comment:
#
# Convert weight to kilograms
#weight_kg = 2.2 * weight_lbs

# Determine number atoms and percentage of universe
num_atoms = (weight_kg / weight_avg_person) * num_atoms_avg_person
percent_of_universe = (num_atoms / num_atoms_universe) * 100

# Display results
print('You contain approximately', format(num_atoms, '.2e'), 'atoms')
print('Therefore, you comprise', format(percent_of_universe, '.2e'),
      '% of the universe')
