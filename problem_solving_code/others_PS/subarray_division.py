#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    segment_count = 0
    if len(s)==1:
        if s[0] == d and m == 1:
            return 1
        else: return 0
    
    for i in range(len(s)):
        if len(s[i:i+m])>=m and sum(s[i:i+m]) == d:
            segment_count+=1

    return segment_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 6

    s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]

    # first_multiple_input = input().rstrip().split()

    d = 18

    m = 7
#   n = int(input().strip())

#     s = list(map(int, input().rstrip().split()))

#     first_multiple_input = input().rstrip().split()

#     d = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
