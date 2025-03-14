
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = sum(candies)
        if n<k:
            return 0
        l, r = 1, max(candies)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            count = sum(c // mid for c in candies)  # Efficient way to count piles
            
            if count >= k:
                res = mid  # Update result
                l = mid + 1  # Try to find a larger valid value
            else:
                r = mid - 1  # Reduce the search space
        
        return res
    # Example
    
obj = Solution()
print(obj.maximumCandies([5,8,6], 3))