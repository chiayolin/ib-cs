# M2.py - Stack Module: Ability to “Peek” in Stack
#
# For the stack module given in Figure 7-15, redesign and re-implement 
# the relevant parts of the module to allow the ability to “peek” into 
# the stack to  find out if a given element is on the stack or not. 
# Write a small program to demonstrate this new version of the stack 
# module.
#
# date:    01/12/2017
# author:  n/a
# license: n/a

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
    Returns and pops the top of stack if not empty. Othereise, returns None.
    """

    if isEmpty(s):
        return None

    item = s[len(s) - 1]
    del s[len(s) - 1]
    
    return item

def peek(s, item):
    
    """
    Returns True if a given element is on the stack else returns False
    """

    return item in s
