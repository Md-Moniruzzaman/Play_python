class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        max_val = 0
        min_i = nums[0]
        for j in range(1,n-1):
            max_k = max(nums[j+1:])
            max_val = max(max_val, (min_i - nums[j]) * max_k)
            min_i = max(min_i, nums[j])
        return max_val
    
# Example
s = Solution()
print(s.maximumTripletValue([12,6,1,2,7])) # 77