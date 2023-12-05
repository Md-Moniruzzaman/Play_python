#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    heighest_record_br_count = 0
    lowest_record_br_count = 0
    h_ch_score = scores[0]
    l_ch_score = scores[0]
    for score in scores:
        if h_ch_score<score:
            heighest_record_br_count+=1
            h_ch_score = score
        elif l_ch_score>score:
            lowest_record_br_count+=1
            l_ch_score=score
    return [heighest_record_br_count,lowest_record_br_count]
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = 9

    # scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(' '.join(map(str, result)))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
