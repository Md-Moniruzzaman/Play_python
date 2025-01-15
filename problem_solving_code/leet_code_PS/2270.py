'''
    Number of ways to split the array
'''

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        n, cnt = len(nums), 0
        for i in nums[:n-1]:
            left_sum += i
            right_sum -= i
            if left_sum >= right_sum:
                cnt += 1
        return cnt
        
    
    
# val = Solution().waysToSplitArray([10,4,-8,7]) # 2
val = Solution().waysToSplitArray([2,3,1,0]) # 2
print(val)