# P7.py
#
# Write a Python program that prompts the user to enter integer values 
# for each of two lists. It then should displays whether the lists are 
# of the same length, whether the elements in each list sum to the same 
# value, and whether there are any values that occur in both lists.
#
# date:    10/31/2016
# author:  Chiayo Lin
# license: GPL 3.0

def get_list(buff):
    char = input("Enter an integer (return to end): ")
    return char == '' and buff or get_list(buff + [int(char)])

def the_same(first, second):
    return first == second and "the same" or "different"

def duplicate_values(first, second):
    return set(first) & set(second) 

print("+-------------------------------+",
      "|    Input for the First List   |",
      "+-------------------------------+", sep = '\n')
first = get_list(list())

print("\n+-------------------------------+",
      "|    Input for the Second List  |", 
      "+-------------------------------+", sep = '\n')
second = get_list(list())

print("\n+-------------------------------+",
      "|           Analysis            |", 
      "+-------------------------------+", sep = '\n')

print("The lists have", the_same(len(first), len(second)), "lengths.")
print("The lists sum to", the_same(sum(first), sum(second)), "values.")

duplicates = duplicate_values(first, second)
print("Values occur in both lists: ", duplicates and duplicates or "{}")
