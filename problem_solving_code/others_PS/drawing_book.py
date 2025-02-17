#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    left_count = p//2
    if n%2 == 0:
        right_count = (n-p+1)//2
    else:
        right_count = (n-p)//2
   
    return min(right_count, left_count)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # p = int(input().strip())

    result = pageCount(6, 5)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
