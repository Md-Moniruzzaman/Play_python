def constructDistanceSequence(n):
    sequence = [0] * (2 * n - 1)
    used = [False] * (n + 1)

    def backtrack(index):
        if index == len(sequence):
            return True
        
        if sequence[index] != 0:
            return backtrack(index + 1)
        
        for num in range(n, 0, -1):
            if not used[num]:
                if num == 1:
                    sequence[index] = 1
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    used[num] = False
                else:
                    if index + num < len(sequence) and sequence[index + num] == 0:
                        sequence[index] = num
                        sequence[index + num] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        sequence[index] = 0
                        sequence[index + num] = 0
                        used[num] = False
        return False

    backtrack(0)
    return sequence

# Example usage:
n = 5
result = constructDistanceSequence(n)
print(result)
