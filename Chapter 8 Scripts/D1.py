# D1.py - Sentence, Word, and Character Count Program
#
# Develop and test a Python program that reads in any given text file and 
# displays the number of lines, words, and total number of characters there 
# are in the file, including spaces and special characters, but not the 
# newline character, '\n'.
#
# Write separate functions for openFile, and countFile. Test openFile with a 
# test driver program. Save this test file as a separate file in a d1 folder.
#
# date:    02/09/2017
# author:  Chiayo Lin
# license: GPL 3.0

def openFile():

    """ 
    Prompts user for file and returns a list
    """

    input_file_opened = False
    while not input_file_opened:
        try:
            input_file = open(input('Enter input file name: '), 'r')
            input_file_opened = True
        except IOError:
            print('Input file not found - please reenter\n')

    return input_file
    
def countFile(input_file):

    """
    returns newline, word, and char counts for a file
    """

    w_count = c_count = l_count = 0
    for line in input_file:
        l_count += 1
        w_count += len(line.split())
        c_count += len(line) - 1


    return (l_count, w_count, c_count)

l_count, w_count, c_count = map(str, countFile(openFile()))

print("Line: " + l_count, 
      "Word: " + w_count, 
      "Char: " + c_count, sep = ", ")
