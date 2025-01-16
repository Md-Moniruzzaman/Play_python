'''
    Unique Length-3 Palindromic Subsequences
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        list1 = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                for k in range(j+1, len(s)):
                    if s[i] == s[k]:
                        val = s[i] + s[j] + s[k]
                        list1.append(val) if val not in list1 else None
        return len(list1)
s = Solution()
print(s.countPalindromicSubsequence("aabca")) # 3
print(s.countPalindromicSubsequence("bbcbaba")) # 4
print(s.countPalindromicSubsequence("adc")) # 0