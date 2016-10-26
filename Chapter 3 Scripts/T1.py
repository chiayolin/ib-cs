# T1.py - Chapter 3 Test Program 1
# 
# date:    10/26/2016
# author:  Chiayo Lin
# license: GPL 3.0

end = 0
while not end:
    integer_1 = int(input("\nEnter first integer: "))
    integer_2 = int(input("Enter second integer: "))
    integer_3 = int(input("Enter last integer: "))

    print((integer_1 in (integer_2, integer_3) or              \
           integer_2 in (integer_1, integer_3)) and            \
           "Duplicate values found" or "Numbers unique")

    end = 0 if input("\nPlay again (y/n)? ").lower()[0] is 'y' \
            else 1
