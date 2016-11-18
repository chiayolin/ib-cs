# D2.py - Holidays Calendar 
#
# Develop and test a Python program that displays the day of the week 
# that the following holidays fall on for a year entered by the user:
#
#   * New Year’s Eve
#   * Valentine’s Day
#   * St. Patrick’s Day (March 17th)
#   * April Fool’s Day (April 1st)
#   * Fourth of July (July 4th)
#   * Labor Day (second tuesday of September)
#   * Halloween 
#   * user’s birthday
#
# Note that Labor Day, as opposed to the other holidays above, does not 
# fall on the same date each year. It occurs each year on the first 
# Monday of September. 
#
# author:  Chiayo Lin
# date:    11/16/2016
# license: MIT License

# return True if n is a number else return False
def is_number(n):
    return n != '' and all(map(lambda k: ord(k) in range(48, 58), n))

# return True if y is a leap year else return False
def is_leap_year(y):
    return (y % 4 and -1 or y % 100 and 1 or y % 400 and -1 or 1) > 0

# return True if m, d, and y make up a valid date else return False
def is_valid_date(m, d, y):
    valid_day = lambda d: d in range(1, d + 1)
    month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    # check if everthing is a number
    if all(map(is_number, [m, d, y])):
        m, d, y = map(int, [m, d, y])
        
        # check if month and day are valid
        return m in range(1, 13) and d in range(1, month_day[m - 1] + 1) or \
               m is 2 and d in range(1, 30) and is_leap_year(y) and 1 or 0
    
    # return False if everything fails
    return False

# prompt the user to enter his birthday and return the date as a list 
def get_bday():
    bday = input("Enter your birthday (MM/DD/YYYY): ")
    
    # validate user's input format
    valid = False
    if len([*filter(lambda x: x == '/', bday)]) >= 2:
        bday = bday.split('/')
        valid = is_valid_date(bday[0], bday[1], bday[2])
    
    # return a list if valid else call get_bday()
    return valid and [*map(int, bday[:3])] or get_bday()

# prompt the user to enter a year and return the year
def get_year():
    y = input("Enter an year: ")
    
    # return an integer if y is a number else call get_year()
    return is_number(y) and int(y) or get_year()

# prompt the user and return True if input contains 'y' 
def get_option(prompt):
    result = input(prompt).lower()
    if result != '':
        return True if result[0] == 'y' else False
    
    return get_option(prompt)

# Sakamoto's the day of week algorithm
def dow(m, d, y):
    # offset for each month
    t = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    
    # check if the year is a leap year
    y -= m < 3
    
    # find the day of week
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7

# return the day of September labour day falls on in year y
def find_labour_day(d, y):
    return dow(9, d, y) == 1 and d or find_labour_day(d + 1, y)

# print the holidays based off given arguments
def print_holidays(year, bday):
    # commonsense that a computer doesn't know
    holidays = (("New Year's Eve", 12, 31), ("St. Patrick Day", 3, 17),
                ("April Fool’s Day", 4, 1), ("Fourth of July", 7, 4),
                ("Labour Day", 9, 1), ("Halloween", 10, 31))
    
    month_name = ("January", "February", "March", "April", "May", 
                  "June", "July", "August", "September", "October", 
                  "November", "December")
    
    day_name = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday")
    
    MONTH = 0; DAY = 1; YEAR = 2 # numeric symbols
    labour_day = 4 # labour day is the fifth element of the tuple
    labour_day_offset = find_labour_day(1, year) - 1
    
    print("\nYour birthday was on", 
          day_name[dow(bday[MONTH], bday[DAY], bday[YEAR])], 
          "in", bday[YEAR], "and it's on", 
          day_name[dow(bday[MONTH], bday[DAY], year)], "in", str(year) + '.\n')

    print("Holidays in", str(year)  + ':')

    NAME = 0; MONTH = 1; DAY = 2 # redefine numeric symbols
    
    # iterate thorugh every element in holidays tuple. this is not a pure 
    # function because it accesses more info than the arguments given.
    def holidays_iter(holiday):
        day = holiday is labour_day and                     \
              holidays[holiday][DAY] + labour_day_offset or \
              holidays[holiday][DAY]

        print(" *", holidays[holiday][NAME], "is on",
              month_name[holidays[holiday][MONTH] - 1], str(day) + ',', 
              day_name[dow(holidays[holiday][MONTH], day, year)] + '.')
        
        if holiday == len(holidays) - 1:
            return None

        return holidays_iter(holiday + 1)
    
    holidays_iter(0)
    print()

def main():
    print_holidays(get_year(), get_bday())

    return None if not get_option("Try again (y/n)? ") else main()
        
__name__ == "__main__" and main() or None
