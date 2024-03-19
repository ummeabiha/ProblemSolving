'''
Every student receives a grade in the inclusive range from 0 to 100.
Any  less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    updated_grade= []
    for i in grades:
        count=0
        if i < 38:
           updated_grade.append(i)
        else:
            #41
            initial_value = i
            while (i%5!=0):
                i+=1
                count+=1
            

            if (count<3):
                updated_grade.append(i)
            else:
                updated_grade.append(initial_value)         
            
    return (updated_grade)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
