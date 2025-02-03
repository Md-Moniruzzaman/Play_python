
""" 
    Longest Stricly increasing or Longest Stricly Decreasing subarray
    You are given an array of integers nums. Return the length of the longest 
    subarray
    of nums which is either 
    strictly increasing
    or 
    strictly decreasing
"""

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        current_inc = 1
        current_dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_inc = current_inc + 1
                current_dec = 1
            elif nums[i] < nums[i-1]:
                current_dec = current_dec + 1
                current_inc = 1
            else:
                current_inc = 1
                current_dec = 1
            max_len = max(max_len, current_inc, current_dec)
        return max_len
    
s = Solution()

print(s.longestMonotonicSubarray([1,4,3,3,2]))
print(s.longestMonotonicSubarray([9, 8, 7, 6, 5, 4]))
print(s.longestMonotonicSubarray([1,10,10]))