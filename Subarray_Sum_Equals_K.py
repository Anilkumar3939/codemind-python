import itertools as t
n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    for j in range(i,n):
        a=[]
        for k in range(i,j+1):
            a.append(l[k])
        l1.append(a)
c=0
for i in l1:
    if sum(i)==m:
        c+=1
print(c)