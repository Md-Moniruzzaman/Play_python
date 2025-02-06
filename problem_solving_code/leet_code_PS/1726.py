'''
    Tuple with Same product
    
'''


def tupleSameProduct(nums: list[int]) -> int:
    from itertools import combinations
    n = len(nums)
    if n == 0:
        return 0
    
    tuple_list = list(combinations(nums, 4))
    count = 0
    for item in tuple_list:
        product = item[0] * item[1] * item[2] * item[3]
        if product / (item[0] * item[1]) == (item[0] * item[1]):
            count+=1
        elif product / (item[0] * item[2]) == (item[0] * item[2]):
            count+=1
        elif product / (item[0] * item[3]) == (item[0] * item[3]):
            count+=1
    
    return count*8
print(tupleSameProduct([1,2,4,5,10]))