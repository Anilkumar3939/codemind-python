a,b=map(int,input().split())
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(a):
    s1=0
    for j in range(b):
        s1+=l[i][j]
    print(s1,end=" ")