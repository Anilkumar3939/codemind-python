n=int(input())
l=list(map(int,input().split()))
l.sort()
a=len(l)//2
l1=l[::-1]
for i in range(1,n,2):
    l1[i],l1[i-1]=l1[i-1],l1[i]
print(*l1)