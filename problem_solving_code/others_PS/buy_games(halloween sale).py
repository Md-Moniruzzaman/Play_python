#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    # games = 0
    # inc_bl = 0
    # new_dc = p
    # while inc_bl+m<=s and p<=s:
    #     print(inc_bl)
    #     if new_dc-d >m:

    #         inc_bl+=(p - d*games)
    #         print(f'inc_bl:{inc_bl}')
    #         new_dc =(p - d*games)
    #         print(f'new_dc:{new_dc}')
    #         games+=1
    #     else:
    #         games+=1
    #         inc_bl+=m
    games = 0
    while  p<=s:
        s = s-p
        p = max(m, p-d)
        games+=1
        
    return games
                
    


if __name__ == '__main__':
   
    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)
    print(f'answer: {answer}')

    
