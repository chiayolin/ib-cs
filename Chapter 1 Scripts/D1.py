# D1.py 
#
# Develop and test a program that allows the user to enter an integer value
# indicating the number of cities to solve for the Traveling Salesman problem. 
# The program should then output the number of years it would take to solve 
# using a brute force-approach. Make use of the factorial function of the math 
# module as shown in Figure 1-28. Estimate the total amount of time it takes by
# using the assumptions given in section 1.1.2:
#
#   10000000 routes/second
#
# date:    08/26/2016
# author:  Chiayo Lin
# license: MIT License
#

import math

compute_time_rps = 10000000 # routes per second
number_of_cities = int(input("How many cities? "))
number_of_routes = math.factorial(number_of_cities)
brute_force_time = (number_of_routes / compute_time_rps) / 60 / 60 / 24 / 365

print(("For {} cities, there are {} possible routes.\n" +
       "It will take a computer about {} years to solve.").
            format(number_of_cities, number_of_routes, brute_force_time))

'''
Have a look at line 19. The constant is off by an order of magnitude.
'''
