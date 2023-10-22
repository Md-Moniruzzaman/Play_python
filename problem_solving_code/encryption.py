import os
import sys
import random
import re
import math

def encryption(s):
    #write your code here
    s = s.replace(' ','')
    row = math.floor(math.sqrt(len(s)))
    col = math.ceil(math.sqrt(len(s)))
    col = col if row*col >=len(s) else col+1

    return s

if __name__ == "__main__":
    s = 'if man was meant to stay on the ground god would have given us roots'

    result = encryption(s)

    print(result)