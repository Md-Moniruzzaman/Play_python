def getHappyString( n: int, k: int) -> str:
    choice = "abc"
    res = []
    total_occurence = 3*(2**(n-1))
    print(total_occurence)
    left,  right = 1, total_occurence
    for i in range(n):
        cur = left
        partition_str = (right - left + 1) // len(choice) 
        print(partition_str)
        for c in choice:
            if k in range(cur, cur + partition_str):
                res.append(c)
                left = cur
                right = cur + partition_str - 1
                choice = "abc".replace(c, '')
                break
            cur += partition_str
    return ''.join(res)
    
print(getHappyString(10, 100))