''' Merge two 2D arrays summing values '''
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0  # Two pointers for nums1 and nums2
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                res.append([id1, val1 + val2])  # Merge values for the same id
                i += 1
                j += 1
            elif id1 < id2:
                res.append([id1, val1])
                i += 1
            else:
                res.append([id2, val2])
                j += 1

        # Add remaining elements from nums1
        while i < n:
            res.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < m:
            res.append(nums2[j])
            j += 1

        return res


# Example
arr1 = [[1, 2], [3, 4]] 
arr2 = [[1, 6], [7, 8]]
s = Solution()
print(s.mergeArrays(arr1, arr2)) # [[6, 8], [10, 12]]