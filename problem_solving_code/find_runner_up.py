if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ls = list(arr)
    ls2 = set(ls)
    ls = list(ls2)
    print(ls)
    ls.remove(max(ls))
    print(max(ls))
    