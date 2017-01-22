# M3.py - Stack Module: Double-Ended Stacks
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

from M3_stack import *

def getDoubleStack():
    
    """
    Creates and returns an empty double-ended stack.
    """

    return getStack()

def isDoubleEmpty(s):
    
    """
    Returns True if stack n empty such that n = 0 indicates the first stack
    and n != 0 indicates the second stack. Otherwise, returns False.
    """
    
    return isEmpty(s)

def topDouble(s, n):
    
    """
    Returns value of the top item of stack n such that n = 0 indicates the
    first stack and n != 0 indicates the second stack, if stack not empty. 
    Othereise, returns None.
    """

    if n == 0:
        return s and s[0] or None
    
    return top(s)   

def pushDouble(s, item, n):
    
    """
    Pushes item on the top of stack n such that n = 0 indicates the first
    stack and n != 0 indicates the second stack.
    """

    if n == 0:
        buff = list(s)
        del s[:]
        s.extend([item] + buff)
        
        return
    
    return push(s, item)

def popDouble(s, n):
    
    """
    Returns top of stack if stack n not empty such that n = 0 indicates 
    the first stack and n != 0 indicates the second stack. Othereise, 
    returns None.
    """

    if n == 0:
        item = s[0]
        del s[:1]
        return item
    
    return pop(s)
