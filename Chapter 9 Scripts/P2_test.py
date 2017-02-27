# P2_test.py
#
# This file is part of P2.py.
#
# date:    02/27/2017
# author:  Chiayo Lin
# license: GPL 3.0

from P2 import moderateDays

week_temps = { "mon" : 70, "tue" : 71, "wed" : 72, "thu" : 90,
               "fri" : 50, "sat" : 32, "sun" : 15 }

print(week_temps)
print("Temperatures between 70 to 79 degrees:", moderateDays(week_temps))
