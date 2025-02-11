'''
    #* Remove All occurrences of a String
    Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.
    Return s after removing all occurrences of part.

    A substring is a contiguous sequence of characters in a string.
'''

def removeOccurrences(s: str, part: str) -> str:
    # s_list = list(s)
    # while True:
    #     index = s.find(part)
    #     if index == -1:
    #         break
    #     del s_list[index:index++len(part)]
    #     s = ''.join(s_list)
    while part in s:
        s = s.replace(part, '', 1)
    return s

print(removeOccurrences("daabcbaabcbc", "abc"))
print(removeOccurrences("axxxxyyyyb", "xy"))