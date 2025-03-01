def applyOprations(nums: list[int])->list[int]:
    res = []
    k = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
        if nums[i] != 0:
            res.append(nums[i])
        else:
            # print('k:',k)
            k+=1
    
    res.append(nums[-1])
    res+= [0]*k
    return res
    
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums[i+1] = 0
    
    
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            val = nums[j]
            nums[j] = nums[i]
            nums[i] = val
            j+=1
            
    return nums
    
print(applyOprations([1,2,2,1,1, 0]))
print(applyOprations([1,0,2,2,0,3,4])) # [1,2,2,3,4,0,0]
print(applyOprations([1,2,3,4])) # [1,2,3,4]
print(applyOprations([0,0,0,1,2,3,4])) # [1,2,3,4,0,0,0]