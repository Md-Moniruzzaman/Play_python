'''You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

'''


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

