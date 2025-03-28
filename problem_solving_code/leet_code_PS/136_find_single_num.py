# take initial value to 0
# loop over through array and XOR with every value
# return the result

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res^=num
        return res
    
# Example
s = Solution()
print(s.singleNumber([4,1,2,1,2]))