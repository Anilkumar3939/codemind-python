m=int(input())
n=int(input())
l=list()
i=m
count=0
while i<=n:
    j=2
    count1=0
    if(i==1):
        count1=1
    else:
        while j<i:
            if(i%j==0):
                count1=1
                break
            else:
                j=j+1
    if(count1==0):
        l.append(i)
        count=count+1
    i=i+1
for i in range(0,count,1):
    print(l[i])