#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    s_um_left = 0
    s_um_right = 0
    for i in range(len(arr)):
        s_um_left+=arr[i][i]
    # print(s_um_left)
    for j in range(len(arr)):
        # print(j, len(arr)-1-j)
        # print(arr[j][len(arr)-1-j])
        s_um_right+=arr[j][len(arr)-1-j]
    # print(s_um_right)
    return abs(s_um_left - s_um_right)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []
    arr = [[11,2,4],[4,5,6],[10,8,-12]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
