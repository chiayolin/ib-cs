# P4.py
#
# Write a Python function named countAllLetters that is given a line read from 
# a text file and returns a list containing every letter in the line and 
# the number of times that each letter appears (with upper/lowercase letters 
# counted together). 
#
#   [Create a file named p4_text.txt for testing.]
#
# date:    02/14/2017
# author:  Chiayo Lin
# license: GPL 3.0

def countAllLetters(line):
    # We want only alphabets (case insensitive).
    tokens = []
    for char in line.lower():
        if char.isalpha():
            tokens += [char]
    
    # Find the unique alphabets in order and save to a list
    unique_alpha = []
    for token in tokens:
        if token not in unique_alpha:
            unique_alpha += [token]
    
    print(unique_alpha)   
    # Count the number of each unique alphabet and save to a list.
    count_alpha = []
    for alpha in unique_alpha:
        counter = 0
        for token in tokens:
            if token is alpha:
                counter += 1
        count_alpha += [counter]
    print(count_alpha)
    
    # Since the elements in unique_alpha and count_alpha are already in
    # order, we can pair them up and save it to another list.
    index = 0
    alpha_list = []
    while index is not len(unique_alpha):
        alpha_list += [(unique_alpha[index], count_alpha[index])]
        index += 1
    
    # Return the resulting list
    return alpha_list

# A small test will do for now
print(countAllLetters("This land was made for you and Me."))
