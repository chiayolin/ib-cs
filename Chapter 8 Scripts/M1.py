# M1.py - Sparse Text Program: User-Selected Letter Removed
#
# Modify the Sparse Text program in section 8.3.4 so that instead of the 
# letter 'e' being removed, the user is prompted for the letter to remove.
#
# date:    02/12/2017
# author:  Chiayo Lin
# license: GPL 3.0

from functools import reduce

def joinList(array):
    return reduce(lambda x, y: x + y, array)

def removeLetter(line, letter = 'e'):
    return joinList(filter(lambda x: x != letter.upper() and   \
                                     x != letter.lower(), line))

def getFile(default_name = "alice_tea_party.txt"):
    name = input("Enter File Name (" + default_name + "): ")

    return open(not name and default_name or name, 'r')

def getLetter():
    return input("Letter to remove: ")[0].lower()

def fileDiff(orig_file, modi_file, letter):
    orig_file_len = sum(map(len, orig_file))
    orig_file.seek(0) # reset file pointer
    modi_file_len = sum(map(len, modi_file))
    
    return (str(orig_file_len - modi_file_len) + " occurences of letter " + \
            letter.upper() + " removed", "Percentage of data lost: "      + \
            format((1  - (modi_file_len / orig_file_len )) * 100, '.1f')  + \
            " %", "Modified text in file 'e_" + orig_file.name + "'")
    
def writeFile(modi_file_src, modi_file_name):
    modi_file = open(modi_file_name, 'w')
    for line in modi_file_src:
        modi_file.write(line)
    
    return modi_file.close()

def M1():
    orig_file = getFile()
    letter_rm = getLetter() 
    modi_file = map(lambda line: removeLetter(line, letter_rm), orig_file)

    writeFile(modi_file, "e_" + orig_file.name) 
    orig_file.seek(0) # reset file pointer

    print('\n', *modi_file, sep = '')
    orig_file.seek(0) # reset file pointer
    print(*fileDiff(orig_file, modi_file, letter_rm), sep = '\n')

    return

__name__ == "__main__" and M1()

