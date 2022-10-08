n=int(input())
l=list(map(int,input().strip().split()))
a=0
for i in range(0,n,1):
    if(l[i]%2!=0):
        a=a+l[i]
print(a)