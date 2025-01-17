'''
    Shift Letters ii (Leet Code 2381)
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        prefix_diff = [0] * (len(s)+1)
        for shift in shifts:
            start, end, direction = shift
            prefix_diff[end+1] += 1 if direction else -1
            prefix_diff[start] += -1 if direction else 1
        
        diff = 0
        res = [ord(c) - ord('a') for c in s]
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i-1] = (res[i-1] + diff) % 26
            
        s = [chr(c + ord('a')) for c in res]
        
        return ''.join(s)
    
s = Solution()
print(s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]])) # ace