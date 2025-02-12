

from collections import defaultdict

def maximumSum( nums: list[int]) -> int:
    n = len(nums)
    max_valu = -1
    for i in range(n):
        print(list(map(int, str(nums[i]))) ,sum(map(int, str(nums[i]))))
        for j in range(i+1, n):
            if sum(map(int, str(nums[i]))) == sum(map(int, str(nums[j]))):
                max_valu = max(max_valu, nums[i] + nums[j])
    return max_valu
            
print(maximumSum([18,43,36,13,7]))