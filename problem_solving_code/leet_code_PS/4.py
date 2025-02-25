''' Medial of two sorted arrays'''

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # nums = nums1 + nums2
    # nums.sort()
    # n = len(nums)
    # if n % 2:
    #     return nums[n // 2 -1]
    # else:
    #     return (nums[n // 2 -1] + nums[(n // 2) ])/2
    
    # For Optimization Means time complexity O(log(m+n))
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is smaller
    
    m, n = len(nums1), len(nums2)
    left_half_size = (m + n + 1) // 2  # The left half should contain this many elements
    
    low, high = 0, m
    
    while low <= high:
        partition1 = (low + high) // 2  # Partition index for nums1
        partition2 = left_half_size - partition1  # Partition index for nums2

        # Get max left and min right values
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        # Correct partition found
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 1:  # Odd length
                return max(maxLeft1, maxLeft2)
            else:  # Even length
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        
        # Move search range
        elif maxLeft1 > minRight2:  
            high = partition1 - 1  # Move left
        else:
            low = partition1 + 1  # Move right

    
print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
print(findMedianSortedArrays([1,2,4,5] , [6,7,9,11,12] ))
