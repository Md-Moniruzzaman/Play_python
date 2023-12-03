#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'similarStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def similarStrings(n, queries):
    # Write your code here
    s = "giggabaj"
    result =''
    for query in queries:
        sub_string = s[query[0]-1:query[1]]
        print(sub_string)
        if len(sub_string)==1:
            result+=str(len(s))
       
    
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    n = 8
    # n = int(first_multiple_input[0])

    q = 4
    # q = int(first_multiple_input[1])

    queries = [[1, 1], [1, 2], [1, 3], [2, 4]]
    # queries = []

    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = similarStrings(n, queries)
    print('\n'.join(map(str, result)))

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
