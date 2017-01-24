# M4.py - Calendar Year Program: Flexible Layout of Months

# Modify the Calendar Year Program so the user can select whether they want 
# the calendar displayed “row oriented” (with January, February, and March 
# in the first row, April, May, and June in the second row, etc.) or “column 
# oriented" (with January, February, March, and April in the first column, 
# May, June, July, and August in the second column, etc.).
#
# date:    01/21/2017
# author:  n/a
# license: n/a

# TODO: Run a Test Tonight

from functools import reduce

def consMonthCal(m, y):
    # Sakamoto's the day of week algorithm
    def _dow(m, d, y):
        # offset for each month
        t = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
        
        # check if the year is a leap year
        y -= m < 3
                                
        # find the day of week
        return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
    
    # Returns True if y is a leap year else return False
    def _isLeapYear(y):
        return (y % 4 and -1 or y % 100 and 1 or y % 400 and -1 or 1) > 0
    
    # Gets a 7-element segment from a list of days
    def _getMonthRow(days, row):
        return days[7 * row : 7 * (row + 1)]
    
    # Constructs the "raw" month calendar
    def _consMonthCal(days, buff = list(), row = 0):
        return _getMonthRow(days, row) and               \
               _consMonthCal(days, buff + [_getMonthRow( \
                             days, row)], row + 1) or buff
    
    month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    month_name = ("January", "February", "March", "April", "May", 
                  "June", "July", "August", "September", "October",
                  "November", "December")

    month_header = [[format(month_name[m - 1], ' ^20')], 
                    ["Su Mo Tu We Th Fr Sa"]]

    initial_offset = ['  '] * _dow(m, 1, y)

    days_list = list(map(lambda c: len(c) == 1 and ' ' + c or c, \
                     map(str, range(1, _isLeapYear(y) and m == 2 \
                                       and 30 or month_day[m - 1] + 1))))
    
    final_offset = ['  '] * (42 - len(days_list))
     
    return ((lambda c: month_header + c + (len(c) != 6 and [[]] or []))( \
            _consMonthCal(initial_offset + days_list + final_offset)))

def consYearCal(y):
    return [[format(y, ' ^64')]] + \
            list(map(lambda m: consMonthCal(m, y), range(1, 13)))

# TODO: PROTOTYPE: This function is not currently in use.
def printYearCal(year_cal, display_option = "row"):
    print(*year_cal[0], '\n')

    if display_option == "row":
        month_offset = 1
        month_increment = 1
        month_counter_offset = 3

        right_most_increment = 3
    else:
        month_offset = 0
        right_most_increment = 1
        month_increment = 4
        month_counter_offset = 8
    
    right_most_month = 4
    while right_most_month < 13 + month_offset:
        row_iter = 0
        while row_iter != 8:
            month_counter = right_most_month - month_counter_offset
            while month_counter != right_most_month:
                print(*year_cal[month_counter][row_iter], end = '  ')
                month_counter += month_increment
            print()
            row_iter += 1
        right_most_month += right_most_increment

    return

def printYearCalRow(year_cal):
    print(*year_cal[0], '\n')
    
    offset = 1
    right_most_month = 4
    while right_most_month <= 13 + offset:
        row_iter = 0
        while row_iter != 8:
            month_counter = right_most_month - 3
            while month_counter != right_most_month:
                print(*year_cal[month_counter][row_iter], end = '  ')
                month_counter += 1
            print()
            row_iter += 1
        right_most_month += 3

    return

def printYearCalCol(year_cal):
    print(*year_cal[0], '\n')
    
    right_most_month = 9
    while right_most_month < 13:
        row_iter = 0
        while row_iter != 8:
            month_counter = right_most_month - 8
            while month_counter != right_most_month + 4:
                print(*year_cal[month_counter][row_iter], end = '  ')
                month_counter += 4
            print()    
            row_iter += 1
        right_most_month += 1
    
    return

def printMonthCal(month_cal, y):
    print(format(reduce(lambda x, y: x + y, filter(lambda c: c != ' ', \
                        *month_cal[0])) + ' ' + str(y), ' ^20'), sep = '')   
    row_iter = 1
    while row != 8:
        print(*month_cal[row_iter], end = '\n')
        row_iter += 1

    return

def main():
    # This main function is too ugly so I have to rewrite it later
    year = int(input("Choose a Year: "))
    month_or_year = input("Month or Year Calendar (month/year): ").lower()[0]
    display_option = input("Display Option (row/column): ").lower()[0]
    
    if month_or_year == 'm':
        month = int(input("Enter a Month: "))
        print()
        printMonthCal(consMonthCal(month, year), year)
    elif month_or_year == 'y' and display_option == 'r':
        print()
        printYearCal(consYearCal(year))
    elif month_or_year == 'y' and display_option == 'c':
        print()
        printYearCalCol(consYearCal(year))
    else:
        print("Invalid option")

    return

__name__ == "__main__" and main() or None
