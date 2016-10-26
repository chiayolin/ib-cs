# T2.py - Chapter 3 Test Program 2
# 
# date:    10/26/2016
# author:  Chiayo Lin
# license: GPL 3.0

word = ''
counter = 0
token = input("Letter to search for: ")

while word != '0':
    word = input("Word to search (0 to end): ")
    counter += word != '0' and token in word and 1 or 0

print(counter, "of those words have an", token)
