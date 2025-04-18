class Solution:
    def compress(self, chars: list[str]) -> int:
        res = ''
        count = 1
        ret = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res += chars[i-1] + str(count) if count > 1 else chars[i-1]
                ret += 2 if count>1 else 1
                count = 1
        res += chars[-1] + str(count) if count > 1 else chars[-1]
        ret += 2 if count>1 else 1
        return ret, list(res)
        
# Example usage
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))  # Output: 6 (["a","2","b","2","c","3"])
print(s.compress(["a"]))  # Output: 1 (["a"])
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))  # Output: 2 (["a","b"])
