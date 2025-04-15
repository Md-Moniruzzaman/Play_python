class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones
    
# Example usage
s = Solution()
print(s.singleNumber([2, 2, 3, 2]))  # Output: 3
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99