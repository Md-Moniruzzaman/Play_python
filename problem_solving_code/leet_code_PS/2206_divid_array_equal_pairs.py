from collections import Counter
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        hash_map = Counter(nums)
        for i in hash_map:
            if not hash_map[i] % 2 == 0:
                return False
        return True
# Example

s = Solution()
print(s.divideArray([3,2,3,2,2,2]))