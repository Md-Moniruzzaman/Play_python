
# 1. Use a difference array (diff) to mark the start and end of meetings efficiently.
# 2. Convert the difference array into a prefix sum to track meeting days.
# 3. Count the number of free days in one pass.

class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        diff = [0]*(days + 2)
        
        for s, e in meetings:
            diff[s] += 1
            diff[e+1] -= 1
        
        met = 0
        miss_days_count = 0
        
        for i in range(1, days + 1):
            met+=diff[i]
            if met == 0:
                miss_days_count+=1
        return miss_days_count
    
# Example
s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
    