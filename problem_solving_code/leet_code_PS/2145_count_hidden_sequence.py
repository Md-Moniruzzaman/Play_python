class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        current_sum = 0
        for d in differences:
            current_sum += d
            min_val = min(min_val, current_sum)
            max_val = max(max_val, current_sum)
        # Calculate the range of valid starting points
        range_start = lower - min_val
        range_end = upper - max_val
        # The number of valid starting points is the range size
        return max(0, range_end - range_start + 1)
# Example usage
s = Solution()
print(s.numberOfArrays([1, -3, 4], 1, 6))  # Output: 2
print(s.numberOfArrays([3, 2, 1, -4], -2, 2))  # Output: 0
print(s.numberOfArrays([4,-7,2], 3, 6))  # Output: 0