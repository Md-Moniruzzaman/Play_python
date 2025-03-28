

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        i, j = len(a) -1, len(b) - 1
        while i>=0 or j>=0 or carry:
            t = carry
            if i>=0:
                t+=int(a[i])
                i-=1
            if j>= 0:
                t+=int(b[j])
                j-=1
            result = str(t%2)+result
            carry = t//2
        return result
        
        
# Example
s = Solution()
print(s.addBinary(a = "11", b = "1"))