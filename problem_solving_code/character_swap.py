
def swap_case(s):
    res_s = ''
    for i in s:
        if i.isupper():
         res_s+=i.lower()
        else:
           res_s+=i.upper()
    return res_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)