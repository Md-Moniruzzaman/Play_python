import string
def print_rangoli(size):
    s = string.ascii_lowercase
    rows = size*2-1
    w = size*4-3
    # l1 = '-'.join(s[size-1::-1]+s[1:size])

    for i in range(1,rows//2+1):
            l = '-'.join(s[size-1:size-i:-1]+s[size-i:n])
            print(l.center(w,'-'))

        
    for i in range(rows//2+1 ,0,-1):
            l2 = '-'.join(s[size-1:size-i:-1]+s[size-i:n])
            print(l2.center(w,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)