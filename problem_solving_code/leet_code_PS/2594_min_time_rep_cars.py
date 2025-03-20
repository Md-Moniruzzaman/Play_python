from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time):
            total_rep_car = 0
            for r in ranks:
                total_rep_car += int(math.sqrt(time//r))
                if total_rep_car>=cars:
                    return True
            return total_rep_car>=cars

        l, r = 1, max(ranks)*(cars**2)
        while l<r:
            mid = (r+l)//2
            if canRepairInTime(mid):
                r = mid
            else:
                l = mid + 1
        return l

# Example

s = Solution()
print(s.repairCars(ranks = [4,2,3,1], cars = 10))
print(s.repairCars(ranks = [5,1,8], cars = 6))