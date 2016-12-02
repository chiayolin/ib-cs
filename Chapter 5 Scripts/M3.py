# M3.py - GPA Calculation Program: Allowing for Plus/Minus Grading
#
# Modify the GPA Calculation program in section 5.2.7 so that it is capable 
# of calculating a GPA for plus / minus letter grades: A, A-, B+, B, B-, 
# and so forth.
#
# date:    12/01/2016
# author:  n/a
# license: n/a

# Semester GPA Calculation

def isValidGrade(grade):
    return all(filter(lambda g: ord(g) in \
                      ([43, 45] + [*range(65, 71)]), grade)])

def isValidCredit(credit):
    return all(filter(lambda n: ord(n) in range(48, 58), credit)

def convertGradeSign(g):
    return g is '-' and (-.3) or g is '+' and (+.3) or 0

def convertGrade(grade):
    if grade[0] == 'F':
        return 0
    
    return (lambda v: v > 4 and 4 or v < 1 and 1 or v)(        \
            4 - (ord(grade[0]) - ord('A')) + convertGradeSign( \
                 len(grade[0]) >= 2 and grade[1] or ''))

# return semester_info as a nested list
def getGrades():
    course_grade = input('Enter grade (hit Enter if done): ')
    num_credits = input('Enter number of credits: ')

    isValidGrade(course_grade) and isValidCredit(num_credits)


def getGrades():
    semester_info = []
    more_grades = True
    empty_str = ''

    is_invalid = lambda g: g != '' and g[0] not in ('A','B','C','D','F')
    
    while more_grades:
        course_grade = input('Enter grade (hit Enter if done): ')
        while is_invalid(course_grade):
            course_grade = input('Enter letter grade received: ')

        if course_grade == empty_str:
            more_grades = False
        else:
            num_credits = int(input('Enter number of credits: '))
            semester_info.append([num_credits, course_grade])

    return semester_info
        
def calculateGPA(sem_grades_info, cumulative_gpa_info):
    sem_quality_pts = 0
    sem_credits = 0
    current_cumulative_gpa, total_credits = cumulative_gpa_info

    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]
        
        sem_quality_pts = sem_quality_pts + \
                          num_credits * convertGrade(letter_grade)
        
        sem_credits = sem_credits + num_credits

    sem_gpa = sem_quality_pts / sem_credits
    new_cumulative_gpa = (current_cumulative_gpa * total_credits + sem_gpa * \
                          sem_credits) / (total_credits + sem_credits)
                   
    return (sem_gpa, new_cumulative_gpa)

# ---- main

# program greeting
print('This program calculates semester and cumulative GPAs\n')

# get current GPA info
if input("Is it your first semester (Y/n)? ").lower() != 'y':
    total_credits = int(input('Enter total number of earned credits: '))
    cumulative_gpa = float(input('Enter your current cumulative GPA: '))
    cumulative_gpa_info = (cumulative_gpa, total_credits)
else:
    cumulative_gpa_info = (0, 0)

# get current semester grade info
print()
semester_grades = getGrades()

# calculate semester gpa and new cumulative gpa
semester_gpa, cumulative_gpa = calculateGPA(semester_grades, 
                                            cumulative_gpa_info)

# display semester gpa and new cumulative gpa
print('\nYour semester GPA is', format(semester_gpa, '.2f'))
print('Your new cumulative GPA is', format(cumulative_gpa, '.2f'))
