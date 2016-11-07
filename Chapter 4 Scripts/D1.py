# D1.py - Morsecode converter
#
# Develop and test a Python program that allows a user to type in a message 
# and have it converted into Morse code, and also enter Morse code and have 
# it converted back to the original message. The encoding of Morse code is 
# given below:
#
#   (TABLE DELETED)
#
# author:  Chiayo Lin
# date:    11/07/2016
# license: MIT License

# morsecode table
code = (('A', ".-"),   ('B', "-..."), ('C', "-.-."), ('D', "-.."), 
        ('E', "."),    ('F', "..-."), ('G', "--."),  ('H', "...."), 
        ('I', ".."),   ('J', ".---"), ('K', "-.-"),  ('L', ".-.."), 
        ('M', "--"),   ('N', "-."),   ('O', "---"),  ('P', ".--."), 
        ('Q', "--.-"), ('R', ".-."),  ('S', "..."),  ('T', "-"),
        ('U', "..-"),  ('V', "...-"), ('W', ".--"),  ('X', "-..-"),
        ('Y', "-.--"), ('Z', "--.."), (' ', ' '))

# 'car' takes a pair as the argument, and returns its head. 
# 'cdr' takes a pair as the argument, and returns its tail. 
# their names are come from Lisp: <https://en.wikipedia.org/wiki/Cons>
def car(pair): return [*pair][0][0]
def cdr(pair): return [*pair][0][1]

print("This is a Morsecode converter, invalid char(s) will be ignored.")

string = ' '
while string:
    # get input from the user and filter the invalid char(s).
    string = [*filter(lambda c: c in map(lambda t: car(t), code), 
               input("Enter a sentence (return to end): ").upper())]

    if string:
        # map each char in the string to a filter that finds the respective
        # morsecode for a char. I do this just to piss Guido van Rossum off.
        print(*map(lambda ch: cdr(filter(lambda x: ch in x, code)), string))

