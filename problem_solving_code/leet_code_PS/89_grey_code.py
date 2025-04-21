class Solution:
    def grayCode(self, n: int) -> list[int]:
        # for i in range(1 << n):
        #     print(i, i >> 1, i ^ (i >> 1))
            # i ^ (i >> 1) generates the Gray code
            # i >> 1 shifts the bits of i to the right by 1 position
            # XORing i with its right-shifted version gives the Gray code
            # yield i ^ (i >> 1)
        return [bin(i ^ (i >> 1))[2::].zfill(n) for i in range(1 << n)]
        # return [i ^ (i >> 1) for i in range(1 << n)]
# Example usage
s = Solution()
print(s.grayCode(2))  # Output: [0, 1, 3, 2]
print(s.grayCode(3))  # Output: [0, 1, 3, 2, 6, 7, 5, 4]