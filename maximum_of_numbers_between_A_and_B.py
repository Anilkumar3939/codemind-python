n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
m=0
for i in l:
    if(a<=i<=b):
        l1.append(i)
        m=1
if(m==1):
    print(max(l1))
else:
    print("-1")