# M6.py - Word Frequency Count Program: Outputting Results to a File
#
# Modify the Word Frequency Count program so that the counts of all words 
# in a given text file are output to a file with the same name as the file 
# read, but with the file extension '.wc' (for 'word count').
#
# date:    02/21/2017
# author:  Chiayo Lin
# license: GPL 3.0

## Word Frequency Count Program

import re

def getFile():
    
    """
    Returns file name and file object as tuple: (file_name, input_file).
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

def countWords(input_file):
    
    """ 
    Returns number of occurrences of search_word in provided file
    """

    tokens = []
    delimiters = "[, \-!?:()\n\'\"]+"
    for line in input_file:
        tokens += [*filter(None, re.split(delimiters, line))]
    
    word_count = {} 
    for token in tokens:
        if token in word_count:
            word_count[token] += 1
        else:
            word_count[token] = 1

    return word_count

def writeResult(word_count, file_name):
    
    """
    Writes result of word count to file ending with '.wc'.
    """

    output_file = open(file_name + ".wc", 'w')
    for word in word_count:
        output_file.write("'" + word + "', " + str(word_count[word]) + "\n")

    return

## main

# program welcome
print('This program will display the number of occurrences of a')
print('specified word within a given text file\n')

file_name, input_file = getFile()
writeResult(countWords(input_file), file_name)

print("Result is written to '" + file_name + ".wc'")

