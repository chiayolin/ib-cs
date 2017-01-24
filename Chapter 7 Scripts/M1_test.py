# M1_test.py - Stack Module: Limited Stack Size
#
# This file is part of M1.py.
#
# date:    01/16/2017
# author:  n/a
# license: n/a

from M1 import *

stack = getStack()
print("Stack Empty?", isEmpty(stack))

for i in range(0, 102):
    if not push(stack, i):
        print(i, "pushed to the stack")
    else:
        print("stack overflow:", i)
