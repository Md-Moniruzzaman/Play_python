def longestCommonPrefix(strs: list[str])->str:
    # Initialize the variables result
    result = ""
    
    # Sorting the list as ascending order and took first and last string
    sorted_list = sorted(strs)
    first_str = sorted_list[0]
    last_str = sorted_list[-1]
    
    # Find out longgest common prefix between those 2 string
    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] != last_str[i]:
            return result
        result+=first_str[i]
            
    return result   


print(longestCommonPrefix(["dog","racecar","car"]))