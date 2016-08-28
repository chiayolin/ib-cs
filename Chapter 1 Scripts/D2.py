# D2.py 
# 
# Based on the information provided about the game of chess in section 1.1.2, 
# develop and test a program that determines how many years it would take 
# for all possible chess games to be played if everyone in the world (regard-
# less of age) played one (unique) chess game a day. Assume the current world 
# population to be 7 billion.
#
# date:    08/26/2016
# author:  Chiayo Lin
# license: MIT License
#

# init
print((lambda possible_games, population: \
    (possible_games / population) / 365)(1e120, 7e9), "years")
