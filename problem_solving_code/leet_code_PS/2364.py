"""
    *Count Number of Bad Pairs
    _summYou are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

    Return the total number of bad pairs in nums.
""" 
from collections import defaultdict

def countBadPairs(nums: list[int]) -> int:
    n = len(nums)
    freq = defaultdict(int)
    total_good_pair = 0
    
    for i in range(n):
        key = nums[i] - i
        total_good_pair += freq[key]
        freq[key] += 1
    print(freq)
    total_pairs = n*(n-1)//2
    print("total_pairs" , total_pairs)
    return total_pairs - total_good_pair


print(countBadPairs([4,1,3,3]))