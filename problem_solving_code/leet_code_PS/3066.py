'''
    Minimum operatin to exceed threshold value
'''

import heapq

def minOperations( nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    count = 0
    while True:
        if nums[0]>=k:
            return count
        else:
            x = nums[0]
            heapq.heappop(nums) 
            y = nums[0]
            heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y)) 
            count+=1
    
    
print(minOperations([2,11,10,1,3], 10))
print(minOperations([1,1,2,4,9], 20))