# D1.py - Metric Conversion
#
# Develop and test a Python program that converts pounds to grams, 
# inches to entimeters, and kilometers to miles. The program should 
# allow conversions both ways.
#
# date:    10/02/2016
# author:  Chiayo Lin
# license: GPL 3.0

from random import randint

BASE = 0; TARGET = 1; VALUE = 2

# return a tuple if the sentence is valid otherwise return None
def parser(string):
    tokens = ("cm", "km", "m", "in", "mi", "g", "kg", "lbs")
    
    # helper functions
    tokenise = lambda string: string.split()
    is_digit = lambda string: string.replace('.', '', 1).isdigit()
    validate = lambda base, target: \
        (base <= 4 and target <= 4) or (base > 4 and target > 4)
    
    # parse the sentence
    value = list(filter(lambda term: is_digit(term), tokenise(string)))
    units = list(filter(lambda term: term in tokens, tokenise(string))) 

    # return None if the sentence doesn't provide enough information
    if len(units) < 2 or len(value) <= 0:
        return None   
    
    # return a tuple if the sentence is valid
    elif validate(tokens.index(units[BASE]), tokens.index(units[TARGET])):
        return (units[BASE], units[TARGET], value[BASE])
    
    # return None if the sentence is invalid
    return None

def unit_converter(value, base, target):
    base_ratio = { "mi" : 160934, "km" : 100000, "in" : 2.54,
            "m" : 100, "cm" : 1, "g" : 0.001, "lbs" : 0.453592, "kg" : 1}
    target_ratio = { "mi" : 6.21371e-6, "km" : 1e-5, "in" : 0.393701, 
            "m" : 0.01, "cm" : 1, "g" : 1000, "lbs" : 2.20462, "kg" : 1 }
    
    return float(value) * base_ratio[base] * target_ratio[target]

def main():
    print("Hello. I would like to help you with unit conversions!\n" +
          "The units I know are cm, m, km, in, mi, g, kg, and lbs\n" +
          "Tell me something like: \"Please convert 15 km to mi\".") 

    # read and parse
    data = parser(input("> "))
    if data is None:
        print("I don't understand what you are talking about :(")
        exit(1)
    result = unit_converter(data[VALUE], data[BASE], data[TARGET])
    
    # print the result
    goodbye = ("Goodbye", "Have a good day", "See you later", "Adios")
    print(data[VALUE], data[BASE], "is", format(result, '.6f'), data[TARGET] + 
        '.', goodbye[randint(0, len(goodbye) - 1)] + '!')

    return 0

__name__ == "__main__" and main() or None
