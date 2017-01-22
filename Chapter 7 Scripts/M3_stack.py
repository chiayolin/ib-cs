# M3.py - Stack Module: Double-Ended Stacks
#
# This file is part of M3.py.
#
# date:    01/12/2017
# author:  n/a
# license: n/a

# stack Module

def getStack():
    
    """
    Creates and returns an empty stack.
    """

    return []

def isEmpty(s):
    
    """
    Returns True if stack 1 empty, otherwise returns False.
    """

    if s == []:
        return True

    return False

def top(s):
    
    """
    Returns value of the top item of stack, if stack not empty.
    Otherwise, returns None.
    """

    if isEmpty(s):
        return None

    return s[len(s) - 1]

def push(s, item):

    """
    Pushes item on the top of stack.
    """

    s.append(item)

    return

def pop(s):

    """
    Returns top of stack if stack 1 not empty. Othereise, returns None.
    """

    if isEmpty(s):
        return None

    item = s[len(s) - 1]
    del s[len(s) - 1]
    
    return item

