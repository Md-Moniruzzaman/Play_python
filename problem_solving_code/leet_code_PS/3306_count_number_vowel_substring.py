class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def trackK(k):
            vowel_count = defaultdict(int)
            non_vowel = 0
            l = 0
            count = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowel_count[word[r]]+=1
                else:
                    non_vowel+=1
                
                while len(vowel_count)==5 and non_vowel>=k:
                    count+= (len(word) - r)
                    if word[l] in 'aeiou':
                        vowel_count[word[l]]-=1
                    else:
                        non_vowel-=1
                    
                    if vowel_count[word[l]] == 0:
                        vowel_count.pop(word[l])
                    l+=1
            return count

        return trackK(k) - trackK(k+1)
                    