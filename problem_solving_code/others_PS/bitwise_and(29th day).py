import math
import os
import random
import re
import sys

def bitwise_and(n, k):
    max_bitwise = 0
    for i in range(1,n+1):
        for j in range(1, i):
            bit_wise = i & j
            if max_bitwise<bit_wise<k:
                max_bitwise = bit_wise
    return max_bitwise

if __name__== "__main__":
    T = int(input().strip())

    for i in range(T):
        n, k = map(int , input().rsplit())
        res = bitwise_and(n,k)
   
    print(res)
            
