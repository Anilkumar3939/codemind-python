n=int(input())
l=list(map(int,input().split()))
d={}
l2=[]
l3=[]
l4=[]
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
while max(d.values())!=0:
    a=max(d.values())
    l1=[]
    for i in d.keys():
        if a==d[i]:
            l1.append(i)
            d[i]=0
    l2.append(l1)
for i in l2:
    i.sort()
    l3.append(i)
for i in l3:
    for j in i:
        l4.append(j)
print(*l4)
        

        
        
    
    
    