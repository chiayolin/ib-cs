# M3.py - Stack Module: Double-Ended Stacks::::
#
# A double-ended stack is essentially a pair of stacks that share a fixed 
# amount of storage (memory). The two stacks are designed so that the top 
# of stack of each begins at each end of a list structure. Each top of 
# stack moves towards the other when an element is pushed, as depicted 
# below. This stack implementation has the advantage of more effectively 
# utilizing a fixed amount of memory than if each stack were allocated 
# its own storage.
#
#                      +-----+-+-+-+-+-+-+-----+
#                      | --> | | | | | | | <-- |
#                      +-----+--+-++-+-+-+-----+
#                        top ^       top ^
#                       (stak 1)    (stack 2)
#
# Modify and test the stack module to behave as a double-ended stack.
#
# date:    01/12/2017
# author:  n/a
# license: n/a

# TODO
# Implement this using one list instead of two list nested in one list

from stack_module import *

def getDoubleStack():
    
    """
    Creates and returns an empty double-ended stack.
    """

    return [getStack(), getStack()]

def isDoubleEmpty(s, n):
    
    """
    Returns True if stack n empty such that n = 0 indicates the first stack
    and n != 0 indicates the second stack. Otherwise, returns False.
    """
    
    return n == 0 and isEmpty(s[n]) or isEmpty(s[1])

def topDouble(s, n):
    
    """
    Returns value of the top item of stack n such that n = 0 indicates the
    first stack and n != 0 indicates the second stack, if stack not empty. 
    Othereise, returns None.
    """

    if n == 0:
        return s[n] and s[n][0] or None
    
    return top(s[1])   

def pushDouble(s, item, n):
    
    """
    Pushes item on the top of stack n such that n = 0 indicates the first
    stack and n != 0 indicates the second stack.
    """

    if n == 0:
        buff = list(s[n])
        del s[n][:]
        s[n].extend([item] + buff)
    
    return push(s[1], item)

def popDouble(s, n):
    
    """
    Returns top of stack if stack n not empty such that n = 0 indicates 
    the first stack and n != 0 indicates the second stack. Othereise, 
    returns None.
    """

    if n == 0:
        item = s[n][0]
        del s[n][:1]
        return item
    
    return pop(s[1])

def main():
    
    """
    Tests
    """

    stack = getDoubleStack()
    print("Stacks empty?", isDoubleEmpty(stack, 0) and \
                           isDoubleEmpty(stack, 1))
    
    for i in range(1, 6):
        pushDouble(stack, i, 0)
        pushDouble(stack, i, 1)
        
        print("Stack:", stack)
        print("Top1: ", topDouble(stack, 0))
        print("Top2: ", topDouble(stack, 1), '\n')

    print("Stacks empty?", isDoubleEmpty(stack, 0) and \
                           isDoubleEmpty(stack, 1))
   
    for i in range(1, 6):
        popDouble(stack, 0)
        popDouble(stack, 1)

        print("Stack:", stack)
        print("Top:1 ", topDouble(stack, 0))
        print("Top:2 ", topDouble(stack, 1), '\n') 
   
    print("Stacks empty?", isDoubleEmpty(stack, 0) and \
                           isDoubleEmpty(stack, 1))

    return

main()

