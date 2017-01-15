# P1.py
#
# Write a function called convertStatus that is passed status code 'f', 's', 
# 'j', or 'r' and returns the string 'freshman', 'sophomore', 'junior', or 
# 'senior', respectively. Design your function so that if an inappropriate 
# letter is passed, an error value is returned. Make sure to include an 
# appropriate docstring with your function.
#
# date:    01/11/2017
# author:  Chiayo Lin
# license: GPL 3.0

def convertStatus(status):
    """
    The function convertStatus takes a status code (one charecter long) as 
    an arugment and returns the coresponding string. The function returns
    a non-empty string on success and an empty string on failure.
    empty string on error.
    
    Flags and return values:
        'f' -->  'freshman'
        's' -->  'sophomore' 
        'j' -->  'junior'
        's' -->  'senior'

    """

    code = ('f', 's', 'j', 'r', '')
    string = ('freshman', 'sophomore', 'junior', 'senior', '')
    
    return dict(zip(code, string))[status in code and status or '']
