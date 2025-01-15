'''
    Number of ways to split the array
'''

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        cnt = 0
        for i in range(1, len(nums)):
            print(nums[:i], nums[i:])
            val = sum(nums[:i])
            if val >= total_sum - val:
                cnt += 1
        return cnt
        
    
    
# val = Solution().waysToSplitArray([10,4,-8,7]) # 2
val = Solution().waysToSplitArray([2,3,1,0]) # 2
print(val)