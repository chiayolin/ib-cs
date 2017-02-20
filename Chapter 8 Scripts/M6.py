# M6.py - Word Frequency Count Program: Outputting Results to a File
#
# Modify the Word Frequency Count program so that the counts of all words 
# in a given text file are output to a file with the same name as the file 
# read, but with the file extension '.wc' (for 'word count').
#
# date:    02/12/2017
# author:  Chiayo Lin
# license: GPL 3.0

## Word Frequency Count Program

import re

def getFile():
    
    """
    Returns the file name and associated file object for reading the
    file  as tuple of the form (file_name, input_file).
    """
    
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print ('Input file not found - please reenter\n')
            
    return (file_name, input_file)

def countWords(input_file, search_word):
    
    """ 
    Returns the number of occurrences of search_word in the provided 
    input_file file object.
    """

    def tokenize(lines):
        tokens = []
        delimiters = "[, \-!?:()\n\'\"]+"
        for line in lines:
            tokens += [*filter(None, re.split(delimiters, line))]
        
        return tokens
   
    return len([*filter(lambda t: t == search_word, tokenize(input_file))])

## main

# program welcome
print('This program will display the number of occurrences of a')
print('specified word within a given text file\n')

# open file to search
file_name, input_file = getFile()

# get search word
search_word = input('Enter word to search: ')
search_word = search_word.lower()

# count all occurrences of search word
num_occurrences = countWords(input_file, search_word)

# display results
if num_occurrences == 0:
    print('No occurrences of word', "'" + search_word + "'",
          'found in file', file_name)
else:
    print('The word', "'" + search_word + "'", 'occurs', num_occurrences,
          'times in file', file_name)
      
