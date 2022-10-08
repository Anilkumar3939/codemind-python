n=int(input())
l=list(map(int,input().strip().split()))
count1=0
count=0
a=0
b=0
for i in range(0,n,1):
    if(i%2==0):
        count=count+1
        a=a+l[i]
    else:
        count1=count1+1
        b=b+l[i]
if(count1>=count):
    print(b-a)
else:
    print(a-b)