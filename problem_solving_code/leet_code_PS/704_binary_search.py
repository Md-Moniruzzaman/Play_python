class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
# Example usage 
s = Solution()
print(s.search([-1,0,3,5,9,12], 9))  # Output: 4
print(s.search([-1,0,3,5,9,12], 2))  # Output: -1