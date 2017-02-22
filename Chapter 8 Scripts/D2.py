# D2.py - Variation on a Sparsity Program
#
# Develop and test a program that reads the text in a given file, and produces 
# a new file in which the first occurrence only of the vowel in each word is 
# removed, unless the removal would leave an empty word (for example, for the 
# word “I”). Consider how readable the results are for various sample text.
#
# date:    02/21/2017
# license: GPL 3.0

import sys, re

def removeVowel(word):
    index = found = 0
    while not (index == len(word) or found):
        found = word[index].lower() in "aeiou"
        index += 1
    
    # index - 1 because it's off by 1
    result = word[:index - 1] + word[index:]
    
    # returns word if removal left empty word (e.g. I)
    return not (result and found) and word or result

def getFile(prompt, flag):
    try:
        return open(input(prompt + ": "), flag)
    
    except IOError:
        sys.stderr.write("Error: file cannot be read.")

def readFile(i_file):
    for line in i_file:
        for word in re.split('(\s+)', line):
            yield word
            
if __name__ == "__main__":
    i_file = getFile("Locate a text file", 'r')
    o_file = open(i_file.name + ".rv", 'w')
    
    for word in readFile(i_file):
        o_file.write(removeVowel(word))

    o_file.close()
