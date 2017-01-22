# M3.py - Stack Module: Double-Ended Stacks
#
# This file is part of M3.py.
#
# date:    01/21/2017
# author:  n/a
# license: n/a

from M3 import *

def main():
    
    """
    Tests
    """

    stack = getDoubleStack()
    print("Stacks empty?", isDoubleEmpty(stack) and \
                           isDoubleEmpty(stack))
    
    for i in range(1, 6):
        pushDouble(stack, i, 0)
        pushDouble(stack, i, 1)
        
        print("Psh1: ", i)
        print("Psh2: ", i)
        print("Stack:", stack)
        print("Top1: ", topDouble(stack, 0))
        print("Top2: ", topDouble(stack, 1), '\n')

    print("Stacks empty?", isDoubleEmpty(stack) and \
                           isDoubleEmpty(stack))
   
    for i in range(1, 6):
        print("Stack:", stack)
        print("Pop1: ", popDouble(stack, 0))
        print("Pop2: ", popDouble(stack, 1))
        print("Stack:", stack)
        print("Top1: ", topDouble(stack, 0))
        print("Top2: ", topDouble(stack, 1), '\n') 
   
    print("Stacks empty?", isDoubleEmpty(stack) and \
                           isDoubleEmpty(stack))

    return

if __name__ == "__main__":
    main()
