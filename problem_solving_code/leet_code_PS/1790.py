'''
    The Solution approach should be:

    - Check if the two strings are of the same length. If not, return False.

    - Check if the two strings are already equal. Return True.

    - Find all the indices where the characters differ between s1 and s2.

    - If there are exactly two differing indices, and swapping the characters at these two indices in s1 makes it equal to s2, then return True.

    - Otherwise, return False.
'''


def areAlmostEqual( s1: str, s2: str) -> bool:
    
    if s1 == s2:
        return True
    
    if len(s1) != len(s2):
        return False
    
    mitchmatch = []
    
        
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mitchmatch.append(i)
            if len(mitchmatch)>2:
                return False
            
    return len(mitchmatch) == 2 and s1[mitchmatch[0]] == s2[mitchmatch[1]] and s1[mitchmatch[1]] == s2[mitchmatch[0]]
        
print(areAlmostEqual("bank", "kanb"))
print(areAlmostEqual("attack", "defend"))
print(areAlmostEqual("kelb", "kelb"))