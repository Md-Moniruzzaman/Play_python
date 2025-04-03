from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # Generate all subsets using bitmasking
        for mask in range(1 << n):  # Loop from 0 to 2^n - 1
            subset = [nums[i] for i in range(n) if (mask & (1 << i))]  # Include elements where bit is set
            print(subset)
            res.append(subset)

        return res

# Example
s = Solution()
print(s.subsets([1, 2, 3]))  # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]