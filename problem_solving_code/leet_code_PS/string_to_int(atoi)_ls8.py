class Solution():
    def myAtoi(s: str)->int:
        # define constants for integer range
        int_max = 2**31 - 1
        int_min = - 2**31
        
        # initiallize variables sign and resutl 
        sign = 1
        result = 0
        index = 0
        
        # remove leading white space of the string
        s = s.lstrip()
        if not s:
            return 0
        
        # Checking if there is is a sign character at the begining
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index =+1
            
       
        # Process each digit character
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check for overflow
            if result > (int_max - digit) // 10:
                return int_max if sign == 1 else int_min
            
            result = result * 10 + digit
            index += 1
        
        # Apply the sign and return the result
        return result * sign
            
            
            
p = Solution

print(p.myAtoi(s='-91283472332'))