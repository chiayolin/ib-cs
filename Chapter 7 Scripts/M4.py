# M4.py - Calendar Year Program: Optional Month / Year Display
#
# Modify the Calendar Year Program so the user can select whether 
# they want to display a complete calendar year, or just a 
# specific calendar month.
#
# date:    01/13/2017
# author:  n/a
# license: n/a

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

def printYearCal(year_cal):
    # An ugly way to print this calendar
    print(*year_cal[0], '\n')
    end = 4
    while end <= 13:
        row = 0
        while row != 8:
            month = end - 3
            while month != end:
                print(*year_cal[month][row], end = '  ')
                month += 1
            print()
            row += 1
        end += 3

    return

def printMonthCal(month_cal, y):
    print(format(reduce(lambda x, y: x + y, filter(lambda c: c != ' ', \
                        *month_cal[0])) + ' ' + str(y), ' ^20'), sep = '')   
    row = 1
    while row != 8:
        print(*month_cal[row], end = '\n')
        row += 1

    return

def main():
    # This main function is too ugly so I have to rewrite it later
    year = int(input("Enter a Year: "))
    month_or_year = input("Print Month or Year Calendar (m/y): ").lower()[0]
    if month_or_year == 'm':
        month = int(input("Enter a Month: "))
        print()
        printMonthCal(consMonthCal(month, year), year)
    elif month_or_year == 'y':
        print()
        printYearCal(consYearCal(year))
    else:
        print("Invalid option")

    return

main()
