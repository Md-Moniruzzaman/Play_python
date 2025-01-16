'''
    Shift Letters ii (Leet Code 2381)
'''

class Solution:
    def shiftChar(self, c: str, shift: list[int])->str:
        abc = "abcdefghijklmnopqrstuvwxyz"
        if shift[-1] == 1:
            for c in s[shift[0]:shift[1]]:
                if c == 'z':
                    s[s.index(c)] = 'a'
                else:
                    s[s.index(c)] = abc[abc.index(c)+1]
        else:
            for c in s[shift[0]:shift[1]]:
                if c == 'a':
                    s[s.index(c)] = 'z'
                else:
                    s[s.index(c)] = abc[abc.index(c)-1]
        return s
                
    
    
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        abc = "abcdefghijklmnopqrstuvwxyz"
        a = list(s)
        for shift in shifts:
            if shift[-1] == 1:
                for i, c in enumerate(a[shift[0]:shift[1]+1]):
                    if c == 'z':
                        a[shift[0]+i] = 'a'
                    else:
                        a[shift[0]+i] = abc[abc.index(c)+1]
            else:
                for i, c in enumerate(a[shift[0]:shift[1]+1]):
                    if c == 'a':
                        a[shift[0]+i] = 'z'
                    else:
                        a[shift[0]+i] = abc[abc.index(c)-1]
        return ''.join(a)
    
s = Solution()
print(s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]])) # ace