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

## init
possible_games = 1e120
population_now = 7e9

## main
# population is divided by 2 because a game needs two people to play
print("It will take about", (possible_games / (population_now / 2)) / 365, 
      "years to play", possible_games, "\nchess games if", int(population_now), 
      "humans play one chess game everyday.")

