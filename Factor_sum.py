l=list(map(int,input().split(",")))
l2=[]
for i in l:
    l1=[]
    for j in range(1,i+1):
        if i%j==0:
            l1.append(j)
    if sum(l1) in l:
        l2.append(i)
l2.sort()
if len(l2)!=0:
    print(*l2)
else:
    print("-1")