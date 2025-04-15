class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        draf = {}
        res = 0
        for num in nums:
            if num not in draf:
                draf[num] = 1
            else:
                draf[num]+=1
        for key, val in draf.items():
        
            if val == 2:
                print(f"key: {key}, val: {val}")
                res^=key
        return res

# Example usage
s = Solution()
print(s.duplicateNumbersXOR([1, 2, 3, 1, 2]))  # Output: 3
print(s.duplicateNumbersXOR([4, 5, 6, 4, 5]))  # Output: 1