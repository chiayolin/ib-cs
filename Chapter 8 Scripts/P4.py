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
    def tokenize(line):
        return [*map(lambda y: y.lower(),                               \
                     filter(lambda x: x.isalpha(), line))]

    def unique(tokens, unique_tokens = []):
        return not tokens and unique_tokens or                          \
               unique([*filter(lambda t: tokens[0] != t, tokens[1:])],  \
                      unique_tokens + [tokens[0]])
    
    def count(unique_tokens, tokens):
        return [*zip(unique_tokens,                                     \
                     map(lambda ut: len([*filter(lambda e: e == ut,     \
                         tokens)]), unique_tokens))]

    return (lambda tokens: count(unique(tokens), tokens))(tokenize(line))

