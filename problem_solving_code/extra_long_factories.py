#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
    n = int(input().strip())

    res = extraLongFactorials(n)
    print(res)
