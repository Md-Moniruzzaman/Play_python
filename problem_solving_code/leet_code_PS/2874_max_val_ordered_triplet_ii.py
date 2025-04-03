from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Step 1: Compute suffix maximum array
        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        print(suffix_max)  # Debugging line to check suffix_max array
        
        # Step 2: Initialize variables for max triplet value calculation
        
        max_val = 0
        max_i = nums[0]  # Track max before j
        
        # Step 2: Iterate over `j` and compute max triplet value
        for j in range(1, n - 1):
            max_k = suffix_max[j + 1]  # Get max_k in O(1) time
            max_val = max(max_val, (max_i - nums[j]) * max_k)
            max_i = max(max_i, nums[j])  # Update max_i
        
        return max_val if max_val > 0 else 0

# Example usage
s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))  # Output: 77
print(s.maximumTripletValue([1, 2, 3]))  # Output: 0
