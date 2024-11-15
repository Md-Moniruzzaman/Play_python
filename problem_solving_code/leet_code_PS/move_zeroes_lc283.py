def moveZeroes(nums: list[int])-> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            val = nums[j]
            nums[j] = nums[i]
            nums[i] = val
            j+=1
            print(nums)
        
    print(nums)
    
moveZeroes([0,1,0,3,12])