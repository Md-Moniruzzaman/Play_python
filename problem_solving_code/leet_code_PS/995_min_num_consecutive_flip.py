

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # def flip(nums, i):
        #     nums[i] = 0 if nums[i] else 1
        # count = 0
        # for i in range(len(nums)-(k-1)):
        #     # print(nums[i])
        #     if nums[i] == 0:
        #         # print(i+k)
        #         for j in range(i,i+k):
        #             flip(nums, j)
        #         count+=1
        # # print(nums)
        # for i in range(1, k+1):
        #     if nums[-i] == 0:
        #         return -1
        
        # return count
        
        # After optimization 
        n = len(nums)
        flip, res = 0, 0
        is_flipped = [0] * n  # Track flips at each index

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]  # Remove the effect of flips that are out of range

            if nums[i] == flip:  # If flip is even, original nums[i] should be 1; if odd, it should be 0
                if i + k > n:
                    return -1  # Not enough elements left to flip

                is_flipped[i] = 1  # Mark a flip at this position
                flip ^= 1  # Toggle the flip state
                res += 1  # Increase the flip count

        return res
    
# Example 
s = Solution()
print(s.minKBitFlips([0,1,0], 1)) # 2
print(s.minKBitFlips([1,1,0], k=2)) # -1
print(s.minKBitFlips([0,0,0,1,0,1,1,0], k = 3)) # 3