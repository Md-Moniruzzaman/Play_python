#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    special_problem= 0
    page_count = 0
    for ar in arr:
        ceil_val = math.ceil(ar/k)
        inc_k = [i for i in range(1,k+1)]
        print(f'ceil_val: {ceil_val}')
        if ceil_val >1:
            
            for i in range( 1,ceil_val+1):
                page_count+=1
                print(page_count)
                print(f'inc_k: {inc_k}')
                special_problem = special_problem + 1 if page_count in inc_k else special_problem
                print(f'special prob: {special_problem}')
                inc_k = [i+k if i+k<=ar else 0 for i in inc_k]
        else:
            page_count+=1
            print(page_count)
            special_problem = special_problem + 1 if page_count<=ar else special_problem
            print(f'special prob: {special_problem}')
    return special_problem
             

# def workbook(n, k, arr):
#     pages = [i for i in range(1, sum(math.ceil(i / k) for i in arr) + 1)]
#     prob_list = []
#     special_count = 0
#     for i in arr:
#         for j in range(math.ceil(i / k)):
#             if i > k:
#                 prob_list.append([a + j * k for a in range(1, k + 1)])
#                 i -= k
#             else:
#                 prob_list.append([a + j * k for a in range(1, i + 1)])
#     book = dict(zip(pages, prob_list))
   
#     for page, problems in book.items():
#         for problem in problems:
#             if problem == page:
#                 special_count += 1
#     return special_count


if __name__ == '__main__':
   

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    n = 10

    # k = int(first_multiple_input[1])
    k = 5

    # arr = list(map(int, input().rstrip().split()))
    arr = [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]

    result = workbook(n, k, arr)
    print(result)

   
