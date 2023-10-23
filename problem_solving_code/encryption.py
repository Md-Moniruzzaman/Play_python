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
    row = row if row*col >=len(s) else row+1
    s_array = []
    for i in range(0,len(s),col):
        s_array.append(s[i:i+col])
    st = ''
    for i in range(col):
        for str in s_array:
            if len(str)>=i+1:
                st += str[i] 
        st+=' '

    return st

if __name__ == "__main__":
    # s = 'if man was meant to stay on the ground god would have given us roots'
    s = 'chill out'

    result = encryption(s)

    print(result)