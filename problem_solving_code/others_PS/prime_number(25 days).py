import math

def is_prime(n):
    if n<=1:
        return False
    sqr_root = math.sqrt(n)
    
    if sqr_root.is_integer():
        return False
    
    for i in range(2, int(sqr_root)+1):
        if n%i == 0:
            return False
    
    return True

T = int(input())

for i in range(T):
    n = int(input())
    
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')
        