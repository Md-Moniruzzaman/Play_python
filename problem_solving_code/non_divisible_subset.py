#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    # ls = []
    # for i in range(len(s)):
        
    #     for j in range(i+1,len(s)):
           
    #         sm = 0
    #         sm = s[i] +s[j]
    #         print(s[i] , s[j] , sm%k)
    #         if sm%k != 0:
    #             ls.append(s[i])
    #             ls.append(s[j])
    # print(set(ls))
    # return len(set(ls))
    rem_count = [0] * k
    for num in s:
        rem_count[num % k] += 1
    print(rem_count)
    # result = 0
    # if rem_count[0] > 0:
    #     result += 1
    # for i in range(1, k // 2 + 1):
    #     if i != k - i:
    #         result += max(rem_count[i], rem_count[k - i])
    #     else:
    #         result += 1
    # return result


if __name__ == '__main__':
   
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])
    k = 7

    # s = list(map(int, input().rstrip().split()))
    s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

    result = nonDivisibleSubset(k, s)
    print(result)

   
