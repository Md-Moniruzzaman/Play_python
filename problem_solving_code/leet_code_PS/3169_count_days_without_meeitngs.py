
# 1. Use a difference array (diff) to mark the start and end of meetings efficiently.
# 2. Convert the difference array into a prefix sum to track meeting days.
# 3. Count the number of free days in one pass.

class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free_day_count = 0
        last_meeting_day = 0
        
        for s, e in meetings:
            if s > last_meeting_day+1:
                free_day_count+= s-(last_meeting_day+1)
            last_meeting_day = max(last_meeting_day, e)
        
        if last_meeting_day < days:
            free_day_count += days - last_meeting_day
        return free_day_count
    
# Example
s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
    