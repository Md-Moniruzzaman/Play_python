# #!/bin/python3
# mine

# import math
# import os
# import random
# import re
# import sys

# list = []


# if __name__ == '__main__':
#     n = int(input().strip())
#     while n>0:
#         remainder = n%2
#         n = n//2
#         list.append(remainder)
        
        
#     list.reverse()
#     list.append(0)
#     # print(list)
#     lst = []
#     # if len(list)==1:
#     #   lst.append(1)

#     count = 0
#     for a in list:
#         if a == 1:
#             count+=1
#         else:
#             lst.append(count)
#             count = 0
        
#     # if list[-1] == 1:
#     #     lst.append(1)

#     lst.sort(reverse=True)
#     print(lst[0])
            
# ctgp

n = int(input())
binary = bin(n)[2:]  # Convert n to binary and remove the '0b' prefix
count = 0
max_count = 0

for digit in binary:
    if digit == '1':
        count += 1
        max_count = max(count, max_count)
    else:
        count = 0

print(max_count)
