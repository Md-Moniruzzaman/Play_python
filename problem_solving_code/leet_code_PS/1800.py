
'''
    #1800. Maximum Ascending Subarray Sum
    
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
'''


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
    