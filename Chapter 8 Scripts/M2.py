# M2.py -  Sparse Text Program: Random Removal of Letters
#
# Modify the Sparse Text program in section 8.3.4 so that instead of a 
# particular letter removed, a percent- age of the letters are randomly 
# removed based on a percentage entered by the user.
#
# date:    02/12/2017
# author:  Chiayo Lin
# license: GPL 3.0

from random import randint

def removeRandom(line):
    index = randint(0, len(line) - 2)

    return line[:index] + line[index + 1:]

def chooseRandom(lines):
    random_line = randint(0, len(lines) - 1)
    while not len(lines[random_line]) - 1:
        random_line = randint(0, len(lines) - 1)

    return random_line

def removePercentage(orig_file, percent):
    modi_file = list(orig_file)
    orig_file.seek(0) # reset file pointer
    
    orig_file_len = sum(map(len, modi_file)) - len(modi_file)
    delta = int(orig_file_len - (orig_file_len * (1 - percent)))
   
    while delta:
        random_line = chooseRandom(modi_file)
        modi_file[random_line] = removeRandom(modi_file[random_line])
        
        delta -= 1

    return modi_file
        
def getFile(default_name = "alice_tea_party.txt"):
    name = input("Enter File Name (" + default_name + "): ")

    return open(not name and default_name or name, 'r')

def fileDiff(orig_file, modi_file):
    orig_file_lin = len(list(orig_file))
    orig_file.seek(0) # reset file pointer
    
    orig_file_len = sum(map(len, orig_file))
    orig_file.seek(0) # reset file pointer
    
    orig_real_len = orig_file_len - orig_file_lin   
    modi_real_len = sum(map(len, modi_file)) - orig_file_lin
    
    return ("Percentage of data lost: "                                  + \
            format((1  - (modi_real_len / orig_real_len )) * 100, '.0f') + \
            "%", "Modified text in file 'e_" + orig_file.name + "'")
    
def writeFile(modi_file_src, modi_file_name):
    modi_file = open(modi_file_name, 'w')
    for line in modi_file_src:
        modi_file.write(line)
    
    return modi_file.close()

def makeHeaderText(string):
    return "\n\033[1m\033[4m" + string + "\033[0m\033[0m\n"

def M2():
    orig_file = getFile()
    percentag = int(input("Enter percentage to remove (%): ")) / 100
    modi_file = removePercentage(orig_file, percentag)
    
    orig_file.seek(0) # reset file pointer
    print(makeHeaderText("Original File:"), *orig_file, sep = '', end = '')

    writeFile(modi_file, "e_" + orig_file.name) 
    orig_file.seek(0) # reset file pointer

    print(makeHeaderText("Modified File:"), *modi_file, sep = '')

    orig_file.seek(0) # reset file pointer
    print(*fileDiff(orig_file, modi_file), sep = '\n')

    return

__name__ == "__main__" and M2()

