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

# get one credit value from user and reprompt if entry is invalid
def getCreditIter(prompt):
    # check if c is valid credit value
    def _isValidCredit(c):
        return all([*map(lambda n: ord(n) in range(49, 58), c)]) \
               and credit != ''

    credit = input(prompt)

    return _isValidCredit(credit) and int(credit) or getCreditIter(prompt)

# get cumulative GPA info
def getCumulativeGPA():
    def _isNumber(n):
        return ord(n) in range(48, 58)

    def _isValidGPA(gpa):
        return gpa != '' and len([*filter(lambda c: c is '.', gpa)]) < 2 \
               and all([*map(lambda c: _isNumber(c) or c is '.', gpa)]) \
               and 0 <= float(gpa) and float(gpa) <= 4

    def _getCurrentGpaIter():
        current_gpa = input("Enter your current cumulative GPA: ")
        
        return float(current_gpa) if _isValidGPA(current_gpa) \
               else _getCurrentGpaIter()
            
    if input("Is it your first semester (y/N)? ").lower() != "y":
        total_credits = getCreditIter("Enter total number of earned credits: ")
        cumulative_gpa = _getCurrentGpaIter()

        cumulative_gpa_info = (cumulative_gpa, total_credits)
    else:
        cumulative_gpa_info = (0, 0)
    
    print()
    return cumulative_gpa_info

# get grades & credits from user
def getGrades():
    # check if g is valid letter grade
    def _isValidGrade(g):
        return all(map(lambda c: ord(c) in ([43, 45] \
               + [*range(65, 71)]), g))
       
    # get one grade from user and reprompt if entry is invalid
    def _getCourseGradeIter():
        grade = input("Enter grade (hit Enter if done): ").upper()
        
        if grade == '': return None
        return _isValidGrade(grade) and grade or _getCourseGradeIter()
    
    # inner wrapper for functions and return list if nothing is entered
    # TODO: fix program crashes if first entry is an empty string
    def _getGradesIter(info):
        grade = _getCourseGradeIter()
        if not grade: return info
        
        credit = getCreditIter("Enter number of credits: ")
        if not credit: return info

        return _getGradesIter(info + [[credit, grade]])

    return _getGradesIter(list())

# convert letter grade to numerical value
def convertGrade(g):
    if g[0] == 'F': return 0
        
    # convert "+" and "-" to numerical offset
    def _convertGradeSign(g):
        return g is '-' and (-0.3) or g is '+' and (+0.3) or 0
    
    return (lambda v: v > 4 and 4 or v < 1 and 1 or v)(4.0 - (ord(g[0]) \
            - ord("A")) + _convertGradeSign(len(g) >= 2 and g[1] or ""))

def calculateGPA(sem_grades_info, cumulative_gpa_info):
    # unpack the info
    current_cumulative_gpa, total_credits = cumulative_gpa_info
    
    # calculate the GPA
    def _calculateGpaIter(k, sem_quality_pts, sem_credits):
        if k == 0:
            sem_gpa = sem_quality_pts / sem_credits
            
            # return semester GPA and new cumulative GPA in a tuple
            return (sem_gpa, (lambda sem_gpa: (current_cumulative_gpa \
                              * total_credits + sem_gpa * sem_credits) \
                              / (total_credits + sem_credits))(sem_gpa))
        
        num_credits, letter_grade = sem_grades_info[-k]
        sem_quality_pts += num_credits * convertGrade(letter_grade)

        sem_credits += num_credits

        return _calculateGpaIter(k - 1, sem_quality_pts, sem_credits)
                   
    return _calculateGpaIter(len(sem_grades_info), 0, 0)

def main():
    # program greeting
    print("This program calculates semester and cumulative GPAs\n")

    # get cumulative GPA info and grades
    cumulative_gpa = getCumulativeGPA()
    semester_gpa = getGrades()

    # calculate semester gpa and new cumulative gpa
    semester_gpa, cumulative_gpa = calculateGPA(semester_gpa, cumulative_gpa)

    # display semester gpa and new cumulative gpa
    print("\nYour semester GPA is", format(semester_gpa, ".2f"))
    print("Your new cumulative GPA is", format(cumulative_gpa, ".2f"))

main()

'''
This program doesn't accept values for earned credits
that are divisible by 10. I looked for the error but the
code is too dense to read easily:

This program calculates semester and cumulative GPAs

Is it your first semester (y/N)? n
Enter total number of earned credits: 100
Enter total number of earned credits: 90
Enter total number of earned credits: 80
Enter total number of earned credits: 70
Enter total number of earned credits: 60
Enter total number of earned credits: 50
Enter total number of earned credits: 40
Enter total number of earned credits: 30
Enter total number of earned credits: 20
Enter total number of earned credits: 10
Enter total number of earned credits: 0
Enter total number of earned credits: 99
Enter your current cumulative GPA:

Can you find it?
'''
