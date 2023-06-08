a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    l=l[1:a]+[l[0]]
print(*l)