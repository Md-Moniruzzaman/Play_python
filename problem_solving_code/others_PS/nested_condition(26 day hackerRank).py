
d1, m1, y1 = map(int,input().split())
d2, m2, y2 = map(int,input().split())
fine = 0
if m2 == m1 and y2== y1 and d1>d2:
    fine = 15*(d1-d2) 
elif m1>m2 and y2 == y1:
    fine = 500* (m1-m2)
elif y1>y2:
    fine = 10000

print(fine)

    