'''
    Unique Length-3 Palindromic Subsequences
'''

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char = set(s)
        pal_cnt = 0
        for c in char:
            left_index = s.index(c)
            right_index = s.rindex(c)
            unique_substr = set(s[left_index+1:right_index])
            pal_cnt += len(unique_substr)
        return pal_cnt
        
s = Solution()
print(s.countPalindromicSubsequence("aabca")) # 3
print(s.countPalindromicSubsequence("bbcbaba")) # 4
print(s.countPalindromicSubsequence("adc")) # 0
print(s.countPalindromicSubsequence("aabcdcagf")) # 5