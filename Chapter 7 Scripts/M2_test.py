# M2_test.py - Stack Module: Ability to “Peek” in Stack
#
# This file is part of M2.py
#
# date:    01/12/2017
# author:  n/a
# license: n/a

import M2 as s

stack = s.getStack()
stack_length = 10

for item in range(0, stack_length):
    print(stack)
    s.push(stack, item)

print()

for item in range(0, stack_length + 3):
    if s.peek(stack, item):
        print(item, "found in the stack.")
    else:
        print(item, "not found in the stack.")
 
print()

while s.pop(stack):
    print(stack)
print(stack)
