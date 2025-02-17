import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
   
    temp_list = []
    for ch in s:
        if len(temp_list)>0 and temp_list[-1] == ch:
            temp_list.pop()
        else:
            temp_list.append(ch)
            
    if len(temp_list)>0:
        return ''.join(temp_list)
    else:
        return 'Empty String'
            
            
    
    
    
if __name__ == '__main__':
    s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'
    result = superReducedString(s)
    print(result)