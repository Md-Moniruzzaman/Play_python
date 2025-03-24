class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        met = [0]*days
        for m in meetings:
            s , e = m[0], m[1]
            while s<=e:
                met[s-1] = 1
                s+=1
        return met.count(0)
    
# Example
s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
    