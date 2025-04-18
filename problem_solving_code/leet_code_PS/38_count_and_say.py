class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n-1):
            cur = ''
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == prev[j-1]:
                    count += 1
                else:
                    cur += str(count) + prev[j-1]
                    count = 1
            cur += str(count) + prev[-1]
            prev = cur
        return prev

# Example usage
s = Solution()
print(s.countAndSay(1))  # Output: "1"
print(s.countAndSay(4))  # Output: "1211"
print(s.countAndSay(5))  # Output: "111221"
                    