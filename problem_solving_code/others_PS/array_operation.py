class Array:
    def __init__(self, arr: list):
        self.arr = arr
        
    def subsequence(self)->list:
        n = len(self.arr)
        res = [[]]
        for i in range(n):
            res += [sub + [self.arr[i]] for sub in res]
        return res
    
    def subArray(self)->list:
        n = len(self.arr)
        res = []
        for i in range(n):
            for j in range(i+1, n+1):
                res.append(self.arr[i:j])
        return res
    
    # Finding subsets of a set
    def subsets(self):

        result = [[]]  # Initialize result with the empty set
        for elem in self.arr:
        
            # Generate new subsets by adding the current
            # element to all existing subsets
            result += [sub + [elem] for sub in result]
        return result
# Example
obj = Array(arr=[1,2,3])
print('Subsequence:', obj.subsequence())
print('SubArray:', obj.subArray())
print('Subsets:', obj.subsets())