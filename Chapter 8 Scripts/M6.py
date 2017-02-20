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

def writeCountWordList(input_file, word_list):
    
    """
    Writes all the word counts base on word_list file object in input_file 
    file object file to a text file called input_file.name + ".wc".
    """
    
    def makeResult(file_name, search_word, num_occurrences):
        return not num_occurrences and "No occurrences of word '" +      \
               search_word + "' found in file '" + file_name + "'\n" or  \
               "The word '" + search_word + "' occurs " +                \
               str(num_occurrences) + " times in file '" + file_name + "'\n"
    
    wc_file = open(input_file.name + ".wc", 'w')

    for search_word in word_list:
        input_file.seek(0) # reset file pointer
        wc_file.write(makeResult(input_file.name, search_word,
                                 countWords(input_file, search_word)))

    return

def getWordList(word_list_file = "M6_text.txt"):

    """
    Returns a list of words without newlines from word_list_file.
    """
    
    word_list = []
    for word in open(word_list_file, 'r'):
        word_list += [word[:-1]]

    return word_list
    
## main

# program welcome
print('This program will display the number of occurrences of a')
print('specified word within a given text file\n')

file_name, input_file = getFile()
writeCountWordList(input_file, getWordList())

print("Result is written to '" + file_name + ".wc'")









