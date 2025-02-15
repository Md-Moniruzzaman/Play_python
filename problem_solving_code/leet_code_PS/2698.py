

class Solution:
    
    def punishmentNumber(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def isValid(i:int, cur: int, target: int, sqr: str ) -> bool:
            if i ==len(sqr):
                return cur == target
            
            if cur>target:
                return False
            
            for j in range(i, len(sqr)):
                segment = sqr[i:j+1]
                if isValid(j+1, cur+int(segment), target, sqr):
                    return True
            return False
            
        
        punis_num  = 0
        for i in range(1, n+1):
            sqr_str =  str(i*i)
            if isValid(0,0, i, sqr_str):
                punis_num+= i*i
        return punis_num
    
obj = Solution()
print(obj.punishmentNumber(37))
print(obj.punishmentNumber(10))