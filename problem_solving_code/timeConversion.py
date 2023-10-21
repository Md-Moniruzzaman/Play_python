#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    med = s[-2:]
    if med == "PM":
        hh = int(s[0:2])
        if hh != 12:
            hh+=12
        s = str(hh) + s[2:8]
    elif med == 'AM':
        hh = int(s[0:2])
        if hh == 12:
            s = '00' + s[2:8]
        else:
            s = s[:8]

    return s

if __name__ == '__main__':
    
    s = '12:05:45AM'

    result = timeConversion(s)
    print(result)

   
