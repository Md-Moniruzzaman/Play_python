if __name__ == '__main__':
    s = input()
    # dic = {
    #     'alnum': 'False',
    #     'alpha': 'False',
    #     'digit': 'False',
    #     'lower': 'False',
    #     'upper': 'False'
    #     }
    # for i in s:
    #     if i.isalnum():
    #         dic['alnum'] = 'True'
    #     if i.isalpha():
    #         dic['alpha'] = 'True'
    #     if i.isdigit():
    #        dic['digit'] = 'True'
    #     if i.isupper():
    #         dic['upper'] = 'True'
    #     if i.islower():
    #         dic['lower'] = 'True'
    # for i in dic:
    #     print(dic[i])
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
       
            
            