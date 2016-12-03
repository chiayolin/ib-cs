# M3.py - GPA Calculation Program: Allowing for Plus/Minus Grading
#
# Modify the GPA Calculation program in section 5.2.7 so that it is capable of 
# calculating a GPA for plus / minus letter grades: A, A-, B+, B, B-, 
# and so forth.
#
# date:    12/01/2016
# author:  n/a
# license: n/a

# Semester GPA Calculation

def convertGradeSign(g):
    return g is '-' and (-0.3) or g is '+' and (+0.3) or 0

def convertGrade(g):
    if g[0] == 'F': return 0

    return (lambda v: v > 4 and 4 or v < 1 and 1 or v)(4.0 - (ord(g[0]) - \
            ord('A')) + convertGradeSign(len(g) >= 2 and g[1] or ''))

def getGrades():
    def _isValidGrade(g):
        return all(filter(lambda g: ord(g) in [43, 45] + \
               [*range(65, 71)], g))
    
    def _isValidCredit(c):
        return all(filter(lambda n: ord(n) in range(49, 58), c))
   
    def _getCourseGradeIter():
        grade = input('Enter grade (hit Enter if done): ')
        
        if grade == '': return None
        return _isValidGrade(grade) and grade or _getCourseGradeIter()

    def _getCourseCreditIter():
        credit = input('Enter number of credits: ')
        
        if credit == '': return None
        return _isValidCredit(credit) and int(credit) or _getCourseCreditIter()

    def _getGradesIter(info):
        grade = _getCourseGradeIter()
        if not grade: return info
        
        credit = _getCourseCreditIter()
        if not credit: return info

        return _getGradesIter(info + [[credit, grade]])

    return _getGradesIter(list())

def calculateGPA(sem_grades_info, cumulative_gpa_info):
    print(sem_grades_info)
    sem_quality_pts = 0
    sem_credits = 0
    current_cumulative_gpa, total_credits = cumulative_gpa_info


    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]
        print(convertGrade(letter_grade), letter_grade)
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
