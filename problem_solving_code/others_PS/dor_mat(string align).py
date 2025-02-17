n,m = map(int,input().split())
c = '-'
c2 = '.|.'

# # top part
# for i in range(n//2):
    
#     print((c*(3*((n//2)-i)))+(c2*i)+c2+(c2*i)+(c*(3*((n//2)-i))))

# print((c*((m-7)//2))+'WELCOME'+(c*((m-7)//2)))

# # bottom part
# for i in range(n//2):
#     print((c*(3*(i+1)))+(c2*((n//2)-(i+1)))+c2+(c2*((n//2)-(i+1)))+(c*(3*(i+1))))

# Optimized code

for i in range(n//2):
    print((c2*(i*2+1)).center(m,'-'))

print('WELCOME'.center(m,'-'))

for i in range(n//2-1,-1,-1):
     print((c2*(i*2+1)).center(m,'-'))
    