def clearDigits( s: str) -> str:
    # s_list = list(s)
    # while True:
    #     digit_index = -1
    #     for i in range(len(s_list)):
    #         if s_list[i].isdigit():
    #             digit_index = i
    #             break
        
    #     if digit_index == -1:
    #         break
        
    #     non_digit_index = digit_index - 1
        
    #     while non_digit_index >= 0 and s_list[non_digit_index].isdigit():
    #         non_digit_index -=1
        
    #     if non_digit_index == -1:
    #         break
        
    #     del s_list[non_digit_index]
    #     del s_list[digit_index - 1]
    # return ''.join(s_list)
    
    rest_s = []
    for i in s:
        if i.isalpha():
            rest_s.append(i)
        else:
            rest_s.pop()
    return ''.join(rest_s)
    
print(clearDigits("abc"))
print(clearDigits("cb34"))
print(clearDigits("cb34h"))