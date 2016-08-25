# M2.py
#
# Modify the Drake’s Equation Program in section 1.7 so that it calculates 
# results for a best case scenario, that is, so that factors p (percentage 
# of stars that have planets), f (percentage of those planets that develop 
# life), i (percentage of those planets that develop intelligent life), and 
# c (percentage of those planets that can communicate with us) are all hard
# -coded as 100%. The value of R should remain as 7. Design the program so 
# that the only values that the user is prompted for are how many planets 
# per star can support life, n, and the estimated number of years 
# civilizations last, L. 
#
# ---------------------------------------------------------------------------
#
# SETI Program
#
# The Drake equation, developed by Frank Drake in the 1960s, attempts to
# estimate how many extraterrestrial civilizations, N, may exist in our
# galaxy at any given time that we might come in contact with,
#
#    N = R * p * n * f * i * c * L
#
# where,
#
#    R ... estimated rate of star creation in our galaxy
#    p ... estimated percent of stars that have planets
#    n ... estimated average number of planets that can potentially support
#          life for each star with planets
#    f ... estimated percent of those planets that actually go on to develop life
#    i ... estimated percent of those planets go on to develop intelligent life
#    c ... estimated percent those that are willing and able to communicate
#    L ... estimated expected lifetime of such civilizations
#
# Given that the value for R, 7 per year, is the least disputed of the values,
# the user will be prompted to enter estimated values for the remaining six 
# factors. The estimated number of civilizations that may be detected in our
# galaxy will then be displayed.
# ---------------------------------------------------------------------------
#

# display program welcome
print('Welcome to the SETI program',
      'This program will allow you to enter specific values related to',
      'the likelihood of finding intelligent life in our galaxy. All',
      'percentages should be entered as integer values, e.g., 40 and not .40',
      sep = '\n', end = '\n')

# get user input
n = int(input('How many planets per star do you think can support life?: '))
L = int(input('Number of years you think civilizations last?: '))

# p, f, i, and c are hard-codeed as 100%
p = f = i = c = 100

# calculate result 
num_detectable_civilizations = 7 * (p / 100) * n * (f / 100) * (i / 100) * (c / 100) * L

# display result
print('Based on the values entered...', 
      'there are an estimated {} potentially detectable civilizations in our galaxy'.
        format(round(num_detectable_civilizations)), sep='\n')
