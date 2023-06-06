n,r,q=map(int,input().split())
l=list(map(int,input().split()))
if r>n:
    r=r%n
for i in range(r):
    l=[l[-1]]+l[:n-1]
for i in range(q):
    a=int(input())
    print(l[a])