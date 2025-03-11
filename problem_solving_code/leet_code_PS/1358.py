''' Number of Substrings Containing All Three Characters '''

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        ch_map = defaultdict(int)
        for r in range(len(s)):
            ch_map[s[r]] += 1
            while len(ch_map) == 3:
                count += (len(s) - r)
                ch_map[s[left]] -= 1
                if ch_map[s[left]] == 0:
                    ch_map.pop(s[left])
                left+=1
        return count
    
# Example
obj = Solution()
print(obj.numberOfSubstrings("abcabc")) # 10
print(obj.numberOfSubstrings("aaacb")) # 3
