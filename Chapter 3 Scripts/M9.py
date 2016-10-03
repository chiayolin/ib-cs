# M9.py - Calendar Month Program: User Entry of Month Name
#
# Modify the  nal version of the Calendar Month program to allow the user 
# to enter a month’s name (e.g., 'January') rather than a number (e.g., 1). 
# Make all appropriate changes in the program as a result of this change.
#
# (Photo Deleted)
#
# date:    10/02/2016
# author:  n/a
# license: n/a

# Calendar Month Program (final correct version)

# init
terminate = False
month_names = ('january', 'february', 'march', 'april', 'may', 'june', 'july',
               'august', 'september', 'october', 'november', 'december')

# program greeting
print('This program will display a calendar month between 1800 and 2099')

while not terminate:
    # get month and year
    month = input('Enter month name (e.g., July | return to quit): ').lower().strip()
    
    if month == '':
        terminate = True
    else:
        while not (month in month_names):
            month = input('INVALID - Enter month name: ').lower().strip()
        # verbal month to a numerical value
        month = month_names.index(month) + 1

        year = int(input('Enter year (yyyy): '))
        
        while year < 1800 or year > 2099:
            year = int(input('INVALID - Enter year (1800-2099): '))

        # determine if leap year
        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
            leap_year = True
        else:
            leap_year = False

        # determine num of days in month
        if month in (1,3,5,7,8,10,12):
            num_days_in_month = 31
        elif month in (4,6,9,11):
            num_days_in_month = 30
        elif leap_year:  # February
            num_days_in_month = 29
        else:
            num_days_in_month = 28
            
        # determine day of the week
        century_digits = year // 100
        year_digits = year % 100

        value = year_digits + (year_digits // 4)

        if century_digits == 18:
            value = value + 2
        elif century_digits == 20:
            value = value + 6
            
        if month == 1 and not leap_year:
            value = value + 1
        elif month == 2:
            if leap_year:
                value = value + 3
            else:
                value = value + 4
        elif month == 3 or month == 11:
            value = value + 4
        elif month == 5:
            value = value + 2
        elif month == 6:
            value = value + 5
        elif month == 8:
            value = value + 3
        elif month == 9 or month == 12:
            value = value + 6
        elif month == 10:
            value = value + 1

        day_of_week = (value + 1) % 7  # 1-Sunday, 2-Monday, ..., 0-Saturday

        # determine month name
        if month == 1:
            month_name = 'January'
        elif month == 2:
            month_name = 'February'
        elif month == 3:
            month_name = 'March'
        elif month == 4:
            month_name = 'April'
        elif month == 5:
            month_name = 'May'
        elif month == 6:
            month_name = 'June'
        elif month == 7:
            month_name = 'July'
        elif month == 8:
            month_name = 'August'
        elif month == 9:
            month_name = 'September'
        elif month == 10:
            month_name = 'October'
        elif month == 11:
            month_name = 'November'
        else:
            month_name = 'December'
        
        # display month, year heading, and indication for leap year
        print('\n', ' ' + month_name, year, leap_year and '(leap year)' or '')

        # display rows of dates
        if day_of_week == 0:
            starting_col = 7
        else:
            starting_col = day_of_week
            
        current_col = 1
        column_width = 4
        blank_char = ' '
        blank_column = format(blank_char, str(column_width))
        
        while current_col < starting_col:
            print(blank_column, end='')
            current_col = current_col + 1
            
        current_day = 1
        
        while current_day <= num_days_in_month:
            if current_day < 10:
                print(format(blank_char, '3') + str(current_day), end='')
            else:
                print(format(blank_char, '2') + str(current_day), end='')

            if current_col < 7:
                current_col = current_col + 1
            else:
                current_col = 1
                print()

            current_day = current_day + 1

        print('\n')
