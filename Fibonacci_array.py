n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)-1):
    if l[i+1]-l[i-1]!=l[i]:
        c=1
if c==0 and l[n-1]==l[n-2]+l[n-3]:
    print("yes")
else:
    print("no")