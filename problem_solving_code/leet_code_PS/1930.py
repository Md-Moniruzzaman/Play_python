'''
    Unique Length-3 Palindromic Subsequences
'''

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left_char = set()
        right_char = Counter(s)
        for m in s:
            right_char[m] -= 1
            for c in left_char:
                if right_char[c] > 0:
                    res.add(c + m + c)
            left_char.add(m)
        return len(res)
        
s = Solution()
print(s.countPalindromicSubsequence("aabca")) # 3
print(s.countPalindromicSubsequence("bbcbaba")) # 4
print(s.countPalindromicSubsequence("adc")) # 0
print(s.countPalindromicSubsequence("aabcdcagf")) # 5