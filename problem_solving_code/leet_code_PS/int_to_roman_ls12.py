def int_to_roman(num:int)->str:
    roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    result = ''
    for i in range(len(dec)):
        while num>=dec[i]:
            result+=roman[i]
            num-=dec[i]
    return str(result)

print(int_to_roman(58))
# MMMDCCXLIX