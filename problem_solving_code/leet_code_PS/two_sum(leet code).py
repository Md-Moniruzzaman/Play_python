lst = [3,3]
# lst1 = lst.sort(reverse=False)
# a = lst.index(7)

class Solution:
    def twoSum(self, nums, target):
        hasmap = {}
        for i in range(len(nums)):
            hasmap[nums[i]] = i
        for i in range(len(nums)-1):
            ls = []
            a = target - nums[i]
            temp = nums[i+1:]
            # temp = nums[i+1:]
            if a in temp:
                print(a)
                indx = hasmap[a]
                ls.append(i)
                ls.append(indx)
                return ls
           
t = Solution()
res = t.twoSum(lst, 6)
print(res)
