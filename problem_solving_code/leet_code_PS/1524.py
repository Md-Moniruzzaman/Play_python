
class Solution:
    def numOfSubarrays(self, arr: list[int])->int:
        mod = 10**9+7
        res = 0
        # n = len(arr)
        # sum_list = []
        # odd_sum_count = 0
        # for i in range(n):
        #     for j  in range(i+1, n+1):
        #         res.append(arr[i:j])
        #         if sum(arr[i:j]) % 2 != 0:
        #             odd_sum_count+=1
        #         sum_list.append(sum(arr[i:j]))
        #         odd_sum_count%=mod
        
        odd_count = 0
        even_count = 1
        prefix_sum = 0
        for ele in arr:
            prefix_sum += ele
            if prefix_sum % 2 == 0:
                res = (res + odd_count) % mod
                even_count += 1
            else:
                res = (res + even_count) % mod
                odd_count += 1
        
        return res
    
# Example

obj = Solution()
print(obj.numOfSubarrays([1,3,5]))
print(obj.numOfSubarrays([1,2,3,4,5,6,7]))