'''
    #* Max sum of a pair with a equal sum of digits
    You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

    Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
'''

from collections import defaultdict

def maximumSum( nums: list[int]) -> int:
    def digit_sum(n:int)->int:
        return sum(map(int, str(abs(n))))
    
    n = len(nums)
    digit_map = {} 
    max_valu = -1
    for num in nums:
        d_sum = digit_sum(num)
        if d_sum in digit_map:
            max_valu = max(max_valu, digit_map[d_sum] + num)
            digit_map[d_sum] = max(digit_map[d_sum], num)
        else:
            digit_map[d_sum] = num
            
    return max_valu
            
print(maximumSum([18,43,36,13,7]))
print(maximumSum([10,12,19,14]))

import heapq
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calculateDigitSum(num):
            sumDigit = 0
            while(num>0):
                d = num % 10
                sumDigit += d
                num = num // 10
            sumDigit += num
            return sumDigit

        digitSumMap = defaultdict(list)
        for n in nums:
            digitSum = calculateDigitSum(n)
            heapq.heappush(digitSumMap[digitSum], n)
            if len(digitSumMap[digitSum]) > 2:
                heapq.heappop(digitSumMap[digitSum])
        
        maxSum = -1
        for digitSum, numList in digitSumMap.items():
            if len(numList) == 2:
                maxSum = max(maxSum, numList[0] + numList[1])
        return maxSum
    
    
class Solution2:
    def maximumSum(self, nums: List[int]) -> int:
        d, mx = dict(), -1

        for num in nums:
            sm, n = 0, num
            while n:
                sm += n % 10
                n //= 10
            if sm in d:
                if d[sm][0] <= num:
                    d[sm][1] = d[sm][0]
                    d[sm][0] = num
                elif d[sm][1] < num:
                    d[sm][1] = num
            else:
                d[sm] = [num, -1]
        
        for k in d:
            if d[k][1] != -1: 
                sm = d[k][0] + d[k][1]
                if sm > mx:
                    mx = sm
        
        return mx