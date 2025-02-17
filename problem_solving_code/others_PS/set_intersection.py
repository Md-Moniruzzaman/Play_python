if __name__=="__main__":
    T1 = int(input())
    roles1 = map(int, input().split())
    s1_roles = set(roles1) 
    T2 = int(input())
    roles2 = map(int, input().split())
    s2_roles = set(roles2)
    num_of_intersection = len(s1_roles.intersection(s2_roles))
    print(num_of_intersection)