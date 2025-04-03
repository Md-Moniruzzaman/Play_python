
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort the array to handle duplicates
        n = len(nums)
        res = set()
        # Generate all subsets using bitmasking
        for mask in range(1<< n):
            subset = tuple(nums[i] for i in range(n) if (mask & (1 << i))) # Include elements where bit is set
            res.add(subset)  # Use a set to avoid duplicates
        # Convert set to list of lists
        return list(map(list, res))

# Example usage
s = Solution()
print(s.subsetsWithDup([1, 2, 3]))  # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
print(s.subsetsWithDup([1, 2, 2]))  # Output: [[], [1], [2], [2], [1, 2], [1, 2], [2, 2], [1, 2, 2]]