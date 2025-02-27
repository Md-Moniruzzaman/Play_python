'''Maximum Absolute Sum of any subarray'''

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        n = len(nums)
        # max_sum = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         max_sum = max(max_sum, abs(sum(nums[i:j])))

        # Now optimize this code using kadane's Algorithm
        max_ending = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            max_ending = max(max_ending, nums[i])
            max_sum = max(max_sum, max_ending)
                
        return max_sum
    
# Example
obj = Solution()
print(obj.maxAbsoluteSum([1,-3,2,3,-4]))
print(obj.maxAbsoluteSum([2,-5,1,-4,3,-2]))