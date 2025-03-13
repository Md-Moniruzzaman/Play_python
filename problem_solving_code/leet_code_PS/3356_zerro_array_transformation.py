''' You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.
'''

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        ''' Got Time Limit Exceeded '''
        # k = 0
        # for i in range(len(queries)):
        #     l, r, val = queries[i]
        #     if sum(nums) !=0:
        #         for j in range(l, r+1):
        #             nums[j] -= min(val, nums[j])
        #         k+=1
        #     else:
        #         break
            
        # return k if sum(nums) == 0 else -1
        
        def can_zero_out(nums: List[int], queries: List[List[int]], k: int) -> bool:
            n = len(nums)
            temp = nums[:]
            diff = [0] * (n + 1)
            
            for i in range(k):
                li, ri, vali = queries[i]
                diff[li] -= vali
                diff[ri + 1] += vali
            
            current_decrement = 0
            for i in range(n):
                current_decrement += diff[i]
                temp[i] += current_decrement
                if temp[i] > 0:
                    return False
            return True

        left, right = 0, len(queries)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_zero_out(nums, queries, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
# Example
obj = Solution()
print(obj.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]])) # 2
print(obj.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]])) # -1


# class Solution:
#     def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
#         k = cur_sum = 0

#         diff_arr = [0] * (len(nums)+1)

#         q_idx = 0


#         for i in range(len(nums)):

#             while cur_sum + diff_arr[i] < nums[i]:
#                 if k == len(queries):
#                     return -1

#                 l, r, val = queries[k]

#                 k += 1

#                 if r < i:
#                     continue

#                 diff_arr[max(l, i)] += val
#                 diff_arr[r+1] -= val

#             cur_sum += diff_arr[i]

#         return k