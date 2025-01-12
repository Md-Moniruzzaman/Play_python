# Maximum Number after spliting a string

# def max_score(s):
#     max_score = 0
#     for i in range(1, len(s)):
#         left = s[:i]
#         right = s[i:]
#         left_score = left.count('0')
#         right_score = right.count('1')
#         max_score = max(max_score, left_score + right_score)
#     return max_score

# For Reduching the time complexity we can use the below code
def max_score(s):
    # calculate the total ones in the string
    total_ones = s.count("1")
    
    # initialize the max score to 0
    max_score = 0
    
    # initializethe left zeroes to 0
    left_zeroes = 0
    
    # initialize the left ones to 0
    left_ones = 0
    
    # iterate over the string
    for i in range(len(s)-1):
        if s[i] == "0":
            left_zeroes += 1  
        else:
            left_ones += 1
        right_ones = total_ones - left_ones
        
        max_score = max(max_score, left_zeroes  + right_ones)
    return max_score

print(max_score("011101")) # 5




