'''
    Shift Letters ii (Leet Code 2381)
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        abc = "abcdefghijklmnopqrstuvwxyz"
        a = list(s)
        for shift in shifts:
            start, end, direction = shift
            if direction == 1:  # Shift forward
                for i in range(start, end + 1):
                    a[i] = chr((ord(a[i]) - ord('a') + 1) % 26 + ord('a'))
            else:  # Shift backward
                for i in range(start, end + 1):
                    a[i] = chr((ord(a[i]) - ord('a') - 1) % 26 + ord('a'))
        
        return ''.join(a)
    
s = Solution()
print(s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]])) # ace