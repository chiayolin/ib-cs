# D1.py - Losing Your Head over Chess
#
# Background Story:
#   The game of chess is generally believed to have invented in India in the 6th
#   century for a rulling king by one of his subjects. The king was supposedly
#   very delighted with the game and asked the subject what he wanted in return.
#   The subject, being clever, asked for one grain of wheat on the first square,
#   two grans of wheat on the second square, four grains of wheat on the third
#   square, and so forth, doubling the amount on each next square. The king tho-
#   ught that this was a modest reward for such an invention. However, the total
#   amount of wheat would have been more than 1,000 times the current would pro-
#   duction.
# 
# The Problem:
#   Now develop and test a Python program that calculates how much wheat this
#   would be in pounds, using the fact that a grain of wheat weighs approximate-
#   ly 1/7,000 of a pound. 
#
# Analysis:
#   The probelm can be modeled using a finite geometric series with 64 elements
#   since there are 64 squares on a modern chessboard. The ratio of this geome-
#   tric sequences is 2 and the first element is 1. By subsituting the given
#   information into the formula, S_n = a * (1 - (r^n)) / ( 1 - r), we will then
#   then get: 
#
#       S_64 = 1 * (1 - (2^64)) / ( 1 - 2)
#    
#   S_64 will be the amount of *grains* the subject gets acording to the specif-
#   ication descreibed in the sotry above. In order to covert the result into 
#   pounds, we will multiply S_64 by 1/7000 since a grain of wheat is about 
#   1/7000 of a pound. We will get 2635249153387079 pounds of wheat at the end.
#
# Implementation:
#   This problem is pretty specific and static, one statement printing the 
#   result of the *algorithm* described above will do.
#
# Date:    09/05/2016
# Author:  Chiayo Lin
# License: GPL 3.0
#

print("The subject will get {} pounds of wheat.". 
    format(int(((1 - (2**64)) / ( 1 - 2)) * (1 / 7000)), ','))
