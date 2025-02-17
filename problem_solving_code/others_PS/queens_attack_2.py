#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # without obstacles
    left =  c_q-1
    right = n - c_q
    up = n - r_q
    down = r_q - 1
    upleft = left if left<=up else up
    upright = right if right<=up else up
    downleft = left if left<=down else down
    downright = right if right<=down else down

    # with obstacles
    for obs in obstacles:
        row = obs[0]
        col = obs[1]

        if row == r_q and col<c_q:
            if c_q-col-1<left:
                left = c_q-col-1

        elif row == r_q and col>c_q:
            if col-c_q-1<right:
                right=col-c_q-1
        
        elif col == c_q and row<r_q:
            if r_q-row-1<down:
                down = r_q-row-1

        elif col == c_q and row>r_q:
            if row-r_q-1<up:
                up = row-r_q-1

        elif row<r_q and col<c_q:
            if r_q-row == c_q-col:
                if r_q-row-1<downleft:
                    downleft = r_q-row-1

        elif row <r_q and col>c_q:
            if r_q - row == col-c_q:
                if r_q-row-1<downright:
                    downright = r_q-row -1

        elif row>r_q and col<c_q:
            if row-r_q == c_q-col:
                if row-r_q-1<upleft:
                    upleft = row-r_q-1

        elif row>r_q and col>c_q:
            if row-r_q == col-c_q:
                if row-r_q-1<upright:
                    upright = row-r_q-1

    total = left + right + up + down + upleft + upright + downleft + downright
    return total



if __name__ == '__main__':
   
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])
    n = 8

    k = 0

    # second_multiple_input = input().rstrip().split()

    # r_q = int(second_multiple_input[0])

    # c_q = int(second_multiple_input[1])
    r_q = 5

    c_q = 4

    obstacles = []
    # obstacles = [[5,5], [4,2], [2,3], ]

    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))
    # print(obstacles)

    result = queensAttack(n, k, r_q, c_q, obstacles)





# def queensAttack(n, k, r_q, c_q, obstacles):#80%
#     # Write your code here
#     ls = []
#     for i in range(c_q, 0, -1):
#         if [r_q,i] in obstacles:
#             break
#         ls.append([r_q,i])
#     for i in range(c_q+1, n+1):
#         if [r_q,i] in obstacles:
#             break
#         ls.append([r_q,i])

#     for i in range(r_q, 0,-1):
#         if [i,c_q] in obstacles:
#             break
#         ls.append([i,c_q])

#     for i in range(r_q+1, n+1):
#         if [i,c_q] in obstacles:
#             break
#         ls.append([i,c_q])
    
#     for i in range(1, n+1):
#         if r_q>=c_q:
#             if r_q +i <=n:
#                 if [r_q+i, c_q+i] in obstacles:
#                     break
#                 ls.append([r_q+i, c_q+i])#top to right 
#     for i in range(1, n+1):
#         if r_q>=c_q:
#             if r_q +i <=n:
#                 if [r_q+i, c_q-i] in obstacles:
#                     break
#                 ls.append([r_q+i, c_q-i])#top to left

#     for i in range(1, n+1):
#         if r_q>=c_q:
#             if c_q - i >=1:
#                 if [r_q -i, c_q-i] in obstacles:
#                     break
#                 ls.append([r_q -i, c_q-i])#down to left

#     for i in range(1, n+1):
#         if r_q>=c_q:
#             if  c_q+i<=n:
#                 if [r_q -i, c_q+i] in obstacles:
#                     break
#                 ls.append([r_q -i, c_q+i])#down to right

#     for i in range(1, n+1):
#         if r_q<c_q:
#              if c_q +i <=n:
#                 if [r_q+i, c_q+i] in obstacles:
#                     break
#                 ls.append([r_q+i, c_q+i])#top to right

#     for i in range(1, n+1):
#         if r_q<c_q:
#              if c_q +i <=n:
#                 if [r_q+i, c_q-i] in obstacles:
#                     break
#                 ls.append([r_q+i, c_q-i])#top to left

#     for i in range(1, n+1):
#         if r_q<c_q:
#              if r_q -i >=1:
#                 if [r_q -i, c_q-i] in obstacles:
#                     break
#                 ls.append([r_q -i, c_q-i])#down to left

#     for i in range(1, n+1):
#         if r_q<c_q:
#              if  c_q+i<=n:
#                 if [r_q -i, c_q+i] in obstacles:
#                     break
#                 ls.append([r_q -i, c_q+i])#down to right

    
#     for i in range(n,0,-1):
#         if r_q and c_q == n:
#             if [i, i] in obstacles:
#                 break
#             ls.append([i,i])

       
#     temp = []
#     for i in ls:
#         if i not in temp:
#             temp.append(i)
       
       
#     temp.remove([r_q,c_q])
#     print(temp)
#     print(len(temp))
#     return len(temp)
# # 



# def queensAttack(n, k, r_q, c_q, obstacles):#50%
#     # Write your code here
#     ls = []
#     for i in range(c_q, 0, -1):
#         if [r_q,i] in obstacles:
#             break
#         ls.append([r_q,i])
#     for i in range(c_q+1, n+1):
#         if [r_q,i] in obstacles:
#             break
#         ls.append([r_q,i])

#     for i in range(r_q, 0,-1):
#         if [i,c_q] in obstacles:
#             break
#         ls.append([i,c_q])

#     for i in range(r_q+1, n+1):
#         if [i,c_q] in obstacles:
#             break
#         ls.append([i,c_q])

#     for i in range(1, n+1):
#         if r_q and c_q == n:
#             ls.append([i,i])
#         elif r_q>=c_q:
#             if r_q +i <=n:
#                 ls.append([r_q+i, c_q+i])#top to right
#                 ls.append([r_q+i, c_q-i])#top to left
#             if c_q - i >=1 and c_q+i<=n:
#                 ls.append([r_q -i, c_q-i])#down to left
#                 ls.append([r_q -i, c_q+i])#down to right
#         elif r_q<c_q:
#             if c_q +i <=n:
#                 ls.append([r_q+i, c_q+i])#top to right
#                 ls.append([r_q+i, c_q-i])#top to left
#             if r_q >=1 and r_q<=n:
#                 ls.append([r_q -i, c_q-i])#down to left
#                 ls.append([r_q -i, c_q+i])#down to right
#     temp = []
#     for i in ls:
#         if i not in temp:
#             temp.append(i)
       
       
#     temp.remove([r_q, c_q])
#     # print(temp)
#     # print(len(temp))
#     return len(temp)
