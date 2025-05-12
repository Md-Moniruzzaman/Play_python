from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        if len(digits) < 3:
            return []
        hash_map = Counter(digits)
        result = []
        for i in range(1, 10):
            if hash_map[i] > 0:
                hash_map[i] -= 1
                for j in range(0, 10):
                    if hash_map[j] > 0:
                        hash_map[j] -= 1
                        for k in range(0, 10, 2):
                            if hash_map[k] > 0:
                                result.append(i * 100 + j * 10 + k)
                        hash_map[j] += 1
                hash_map[i] += 1
        return result
    
# Example usage
s = Solution()
print(s.findEvenNumbers([2, 1, 3, 0]))  # Output: [102,120,130,132,210,230,302,310,312,320]
print(s.findEvenNumbers([2, 2, 8, 8, 2]))  # Output: [222,228,282,288,822,828,882]
print(s.findEvenNumbers([3,7,5]))  # Output: []