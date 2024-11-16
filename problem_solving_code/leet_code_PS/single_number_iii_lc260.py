def singleNumber(nums: list[int])->list[int]:
    arr = []
    for i in range(len(nums)):
        
        if nums[i] not in arr:
            arr.append(nums[i])
        else:
            arr.remove(nums[i])
    return arr

print(singleNumber([-1,0]))