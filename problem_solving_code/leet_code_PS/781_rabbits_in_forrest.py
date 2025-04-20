class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        rabbit_count = 0
        hash_map = {}
        for i in answers:
            # print('before:' ,i, hash_map)
            if i == 0:
                rabbit_count += 1
            elif i in hash_map and hash_map[i] == i+1:
                rabbit_count += i + 1
                hash_map[i] = 1
                
            elif i in hash_map and hash_map[i] < i + 1:
                hash_map[i] += 1
            elif i not in hash_map:
                hash_map[i] = 1
            # print('after:' ,i, hash_map)
        # print(hash_map, rabbit_count )
        for i in hash_map:
            if hash_map[i] > 0:
                rabbit_count += i + 1
        return rabbit_count

# Example usage
s = Solution()
print(s.numRabbits([1, 0, 1, 0, 0]))  # Output: 5
print(s.numRabbits([10, 10, 10]))  # Output: 11
print(s.numRabbits([0, 0, 0, 0]))  # Output: 4
print(s.numRabbits([0,0,1,1,1]))  # Output: 4
