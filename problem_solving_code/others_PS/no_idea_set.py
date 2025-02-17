def happiness(arr_test, arr_A, arr_B):
    # your code goes here
    happy = 0
    for i in arr_test:
        if i in arr_A :
            happy+=1
        if i  in arr_B:
            happy-=1
        else:
            pass
    return happy

if __name__ == '__main__':
    n,m = map(int, input().split())
    arr_test,arr_A, arr_B = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
    # arr_n = {1,5,3}
    # arr_m = {3,1}
    # arr_test = {5,7}
    result = happiness(set(arr_test), set(arr_A), set(arr_B))
    print(result)