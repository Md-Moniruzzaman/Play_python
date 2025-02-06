'''
    Tuple with Same product
    
    Correct Approach:
    ------------------
    The problem can be efficiently solved using a frequency map to count pairs of elements with the same product. Here's the optimized approach:

    1. Count Pairs by Product:

    For every pair of elements (a, b) where a < b, compute their product and track how many times each product occurs using a dictionary.

    2. Calculate Valid Tuples:

    For each product p that occurs k times, the number of valid tuples is given by the combination formula C(k, 2) * 8. This accounts for choosing 2 distinct pairs (each contributing 8 ordered permutations).
    
'''


from itertools import combinations
from collections import defaultdict

def tupleSameProduct(nums: list[int]) -> int:
    product_count = defaultdict(int)
    
    for a, b in combinations(nums, 2):
        product_count[a*b]+=1    
    
    total_count = 0
    
    for count in product_count.values():
        if count >= 2:
            total_count += count * (count - 1) *4
        
    return total_count

print(tupleSameProduct([1,2,4,5,10]))
print(tupleSameProduct([2,4,5,10]))
print(tupleSameProduct([2,4,5,10,23,16]))
print(tupleSameProduct([2,4,5,10,23,16,20,50,90]))
print(tupleSameProduct([200,444,555,666,777,888,999,1000]))