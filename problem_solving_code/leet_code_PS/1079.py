
from collections import Counter
def numTilePossibilities(tiles: str) -> int:
    count = Counter(tiles)
    print(count)

    def backTracking():
        ways = 0
        for c in count:
            
            if count[c]>0:
                count[c]-=1
                ways += 1
                print('Before 1:',count[c])
                ways += backTracking()
                print('Before 2:',count[c])
                count[c]+=1
                print('after:',count[c])
        return ways

    return backTracking()

print(numTilePossibilities('AAB'))