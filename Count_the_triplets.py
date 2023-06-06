import itertools as t
n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    x=list(t.combinations(l,2))
    c=0
    for i in x:
        if sum(i) in l:
            c+=1
    if c==0:
        print("-1")
    else:
        print(c)