#!/bin/python3

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
    # Write your code here
    # rounded_grades = []
    # for grade in grades:
    #     if grade>=35:
    #         if (grade + 1) %5 == 0:
    #             rounded_grades.append(grade + 1)
    #         elif (grade + 2) % 5 == 0:
    #             rounded_grades.append(grade + 2)
    #         else:
    #             rounded_grades.append(grade)
    #     else:
    #         rounded_grades.append(grade)
    # return rounded_grades
    return [grade+1 if (grade+1)%5==0 and grade>=35 else grade+2  if (grade+2)%5 == 0 and grade>=35 else grade for grade in grades]

if __name__ == '__main__':
    

    # grades_count = int(input().strip())

    grades = [80,  96, 18, 73, 78, 60, 60, 15,45,15,10,5,46,87,33,60,14,71]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)