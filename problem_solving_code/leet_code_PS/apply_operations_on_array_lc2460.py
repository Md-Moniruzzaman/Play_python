def applyOprations(nums: list[int])->list[int]:
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
    
    
applyOprations([1,1,2,1,1])