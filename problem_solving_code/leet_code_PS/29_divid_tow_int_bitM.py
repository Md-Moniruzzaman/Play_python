import time
start = time.time()
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        if sign * quotient < -2**31:
            return -2**31
        elif sign * quotient > 2**31 -1:
            return 2**31 - 1
        else:
            return sign * quotient 
        


# Example
s = Solution()
print(s.divide(0, 3)) # 3
print(s.divide(2148473647, 1)) # -2
print(s.divide(2147483648, 1)) # 3
print(s.divide(-2147483649.654, 1)) # 3
end = time.time()
print(f"Execution time: {end - start:.6f} seconds")