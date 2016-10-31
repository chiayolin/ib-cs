# T1.py - Chapter 3 Test Program 1
# 
# date:    10/26/2016
# author:  Chiayo Lin
# license: GPL 3.0

end = 0
while not end:
    num_1 = int(input("\nEnter first integer: "))
    num_2 = int(input("Enter second integer: "))
    num_3 = int(input("Enter last integer: "))

    print((num_1 in (num_2, num_3) or                          \
           num_2 in (num_1, num_3)) and                        \
           "Duplicate values found" or "Numbers unique")

    end = 0 if input("\nPlay again (y/n)? ").lower()[0] is 'y' \
            else 1
