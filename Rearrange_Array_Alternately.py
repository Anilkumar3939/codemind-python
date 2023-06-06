n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l1=[]
    x=-1
    for i in range(a//2):
        l1.append(l[x])
        l1.append(l[i])
        x-=1
    if a%2!=0:
        l1.append(l[a//2])
        
    print(*l1)