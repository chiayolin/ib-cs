# M1. Stack Module: Limited Stack Size
#
# For the stack module given in Figure 7-15, suppose that the implementation 
# is to limit stacks to no more than 100 items. Redesign and re-implement 
# the relevant parts of the module that need to be changed. Write a small 
# program to demonstrate this new version of the stack module.
#
# date:    01/16/2017
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
    Pushes item on the top of stack and returns 1 on overflow.
    """
    
    return len(s) > 100 and 1 or s.append(item)

def pop(s):

    """
    Returns top of stack if stack 1 not empty. Othereise, returns None.
    """

    if isEmpty(s):
        return None

    item = s[len(s) - 1]
    del s[len(s) - 1]
    
    return item

def main():
    
    """
    Tests
    """

    stack = getStack()
    print("Stack Empty?", isEmpty(stack))
    
    for i in range(0, 102):
        if not push(stack, i):
            print(i, "pushed to the stack")
        else:
            print("stack overflow:", i)

main()
