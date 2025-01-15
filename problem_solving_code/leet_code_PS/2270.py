'''
    Number of ways to split the array
'''

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        pre = [0]
        cnt = 0
        for i in range(len(nums)-1):
            pre.append(pre[-1] + nums[i])
            if pre[-1] >= total_sum - pre[-1]:
                cnt += 1
        return cnt
        
    
    
# val = Solution().waysToSplitArray([10,4,-8,7]) # 2
val = Solution().waysToSplitArray([2,3,1,0]) # 2
print(val)