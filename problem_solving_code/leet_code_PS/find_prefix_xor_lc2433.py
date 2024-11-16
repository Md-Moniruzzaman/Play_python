def findArray(pref: list[int])->list[int]:
    # res = []
    # res.append(pref[0])
    # for i in range(len(pref)-1):
    #     res.append(pref[i] ^ pref[i+1])
    # return res
    for i in range(len(pref)-1, 0, -1):
        pref[i] = pref[i]^pref[i-1]
    return pref
    
print(findArray([5,2,0,3,1]))