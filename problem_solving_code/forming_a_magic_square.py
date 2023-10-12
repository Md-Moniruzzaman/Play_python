
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    ls = []
    ms = [ 
            [ [ 8, 1, 6 ], [ 3, 5, 7 ], [ 4, 9, 2 ] ], 
            [ [ 6, 1, 8 ], [ 7, 5, 3 ], [ 2, 9, 4 ] ], 
            [ [ 4, 9, 2 ], [ 3, 5, 7 ], [ 8, 1, 6 ] ], 
            [ [ 2, 9, 4 ], [ 7, 5, 3 ], [ 6, 1, 8 ] ], 
            [ [ 8, 3, 4 ], [ 1, 5, 9 ], [ 6, 7, 2 ] ], 
            [ [ 4, 3, 8 ], [ 9, 5, 1 ], [ 2, 7, 6 ] ], 
            [ [ 6, 7, 2 ], [ 1, 5, 9 ], [ 8, 3, 4 ] ], 
            [ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ], 
        ] 
    for k in range(len(ms)):
        ls1 = []
        for i in range(0,3):
            for j in range(0,3):
                res = abs(s[i][j] - ms[k][i][j])
                ls1.append(res)
            
        ls.append(sum(ls1))
    print(ls)

    return min(ls)

if __name__ == '__main__':
   
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

   
