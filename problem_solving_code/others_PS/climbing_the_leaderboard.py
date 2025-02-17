#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# def climbingLeaderboard(ranked, player):
#     # Write your code her
#     rk = list(sorted(set(ranked), reverse=True))
#     pl = sorted(player, reverse=True)
#     ls = []
#     rank = 0
#     for i in rk:
#         if i<=pl[0]:
#             rank+=1
#             ls.append(rank)
#             ind = pl
#             for i in range(len(ind)):
#                 if pl[i] == pl[i+1]:
#                     ls.append(rank)
#                     pl.pop(0)
#                 else:
#                     pl.pop(0)
#                     break
            
#         else:
#             rank+=1
#     print(pl)
#     for i in pl:
#         rank+=1
#         ls.append(rank)
      
#     print(sorted(ls, reverse=True))
#     return sorted(ls, reverse=True)


def climbingLeaderboard(ranked, player):
    ranks = list(sorted(set(ranked), reverse=True))
    result = []
    for score in player:
        while ranks and score >= ranks[-1]:
            ranks.pop()
        result.append(len(ranks)+1)
    return result

if __name__ == '__main__':
   
    ranked_count = int(7)

    ranked = [100, 100, 50, 40, 40, 20, 10]

    player_count = int(6)

    player = [5, 25, 25, 50,50, 120]

    result = climbingLeaderboard(ranked, player)



