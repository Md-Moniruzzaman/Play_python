

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1
        count = 0
        for i in range(len(nums)-(k-1)):
            # print(nums[i])
            if nums[i] == 0:
                # print(i+k)
                for j in range(i,i+k):
                    flip(nums, j)
                count+=1
        # print(nums)
        for i in range(1, k+1):
            if nums[-i] == 0:
                return -1
        
        return count
    
# Example 
s = Solution()
print(s.minKBitFlips([0,1,0], 1)) # 2
print(s.minKBitFlips([1,1,0], k=2)) # -1
print(s.minKBitFlips([0,0,0,1,0,1,1,0], k = 3)) # 3