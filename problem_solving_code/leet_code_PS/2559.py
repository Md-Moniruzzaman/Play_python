'''
    Count Vowel Strings in range
'''
class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        prefix_cnt = [0]
        
        for w in words:
            prefix_cnt.append(prefix_cnt[-1])
            if w[0] in vowels and w[-1] in vowels:
                prefix_cnt[-1] = prefix_cnt[-1] + 1
            
        res = [] 
        for l, r in queries:
            res.append(prefix_cnt[r + 1] - prefix_cnt[l])
            
        return res
        
        
s = Solution()
queries = [[4, 4],[6, 17],[10, 17],[9, 18],[17, 22],[5, 23],[2, 5],[17, 21],[5, 17],[4, 8],[7, 17],[16, 19],[7, 12],[9, 20],[13, 23],[1, 5],[19, 19]]
words = ["ibzmxvzjxfddcuzenspdcbwiojiqfa","mwguoaskvramwgiweogzulcinycosovozppl","uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs","uivcdsboxnraqpokjzaayedf","yalc","bbhlbmpskgxmxosft","vigplemkoni","krdrlctodtmprpxwditvcps","gqjwokkskrb","bslxxpabivbvzkozzvdaykaatzrpe","qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi","siqbezhkohmgbenbkikcxmvz","ddmaireeouzcvffkcohxus","kjzguljbwsxlrd","gqzuqcljvcpmoqlnrxvzqwoyas","vadguvpsubcwbfbaviedr","nxnorutztxfnpvmukpwuraen","imgvujjeygsiymdxp","rdzkpk","cuap","qcojjumwp","pyqzshwykhtyzdwzakjejqyxbganow","cvxuskhcloxykcu","ul","axzscbjajazvbxffrydajapweci"]
# queries = [[0,2],[1,4],[1,1]] 
# words = ["aba","bcb","ece","aa","e"]
val = s.vowelStrings(words=words, queries=queries) # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(val)