from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            """ Returns a boolean list where prime[i] is True if i is prime """
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            
            for i in range(2, int(math.sqrt(n)) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return is_prime

        # Generate primes in range [left, right]
        prime_flags = sieve(right)
        primes = [num for num in range(left, right + 1) if prime_flags[num]]

        # If fewer than 2 primes exist, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]

        # Find the closest prime pair
        min_diff = float('inf')
        res = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i], primes[i + 1]]

        return res
