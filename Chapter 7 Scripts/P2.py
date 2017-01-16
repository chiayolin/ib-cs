# P2.py
#
# Write a function called palindromeChecker using iteration to return True
# if aprovided string is a palindrome, and False otherwise. Make sure to 
# include docstring speci cation for the function.
#
# date:    01/16/2017
# author:  Chiayo Lin
# license: GPL 3.0

def palindromeChecker(string):
    
    """
    palindromeChecker(string) takes one string as its argument and
    returns True if the string is a palindrome else returns false.
    """

    return (lambda s: s == s[::-1])(string.lower())
