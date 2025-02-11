

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