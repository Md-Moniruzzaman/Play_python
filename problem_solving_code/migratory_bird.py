#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here

    dic_typeId = {each:arr.count(each)   for each in range(1, 6) if each in arr}
    # return count_typeId.index(max(count_typeId))+1
    # arr.sort()
    # dic = {} 
    # for bird in arr:
    #     dic[bird] = dic.get(bird,0) + 1
    for k, v in dic_typeId.items():
        if v == max(dic_typeId.values()):
            return k
    
   
    # print(dic_typeId)
   
    

if __name__ == '__main__':

    # arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # arr = [1,4,4,4,3,3,5,3]

    result = migratoryBirds(arr)
    print(result)

  