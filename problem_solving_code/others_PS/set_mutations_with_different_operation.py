


if __name__=="__main__":
    T1 = int(input())
    set_A = set(map(int, input().split()))
    T2 = int(input())
    for _ in range(T2):
        op, _ = input().split()
        set_B = set(map(int, input().split()))
        if op=='intersection_update':
            set_A.intersection_update(set_B)
        elif op=='update':
            set_A.update(set_B)
        elif op == "symmetric_difference_update":
            set_A.symmetric_difference_update(set_B)
        elif op=="difference_update":
            set_A.difference_update(set_B)
    
    print(sum(set_A))
   