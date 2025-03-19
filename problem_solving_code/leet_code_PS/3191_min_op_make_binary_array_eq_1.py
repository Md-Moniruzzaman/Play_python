
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip(nums, i)
                flip(nums, i+1)
                flip(nums, i+2)
                count+=1
        if not nums[-1] or not nums[-2]:
            return -1
        return count

#Example
s = Solution()
print(s.minOperations([0,1,1,1,0,0])) #3

