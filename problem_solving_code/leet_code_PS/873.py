''' Length of longest Fibonacci-like subsequence'''

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_set = set(arr)
        fib_len = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                pre, cur = arr[i], arr[j]
                nxt = pre + cur
                n = 2
                while nxt in arr_set:
                    n+=1
                    pre, cur = cur, nxt
                    nxt = pre + cur
                    fib_len = max(fib_len, n)

        return fib_len

# Example
s = Solution()
print(s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))