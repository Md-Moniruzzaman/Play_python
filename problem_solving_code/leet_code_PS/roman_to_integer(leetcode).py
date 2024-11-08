class Solution:
    def romanToInt(self, s: str)->int:
        self.roman = {"I":1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.number = 0

        for i in range(len(s)-1):
            if self.roman[s[i]] < self.roman[s[i+1]]:
                self.number -= self.roman[s[i]]
            else:
                self.number += self.roman[s[i]]
        return self.number + self.roman[s[-1]]
    
if __name__ == "__main__":
    s = str(input())
    sol = Solution()
    print(sol.romanToInt(s))