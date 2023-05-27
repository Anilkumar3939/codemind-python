n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
r=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)

for i in range(len(l)):
    if(i<len(l2)):
        r.append(l2[i])
    if(i<len(l1)):
        r.append(l1[i])
if(len(l)%2!=0):
    r.append(0)
print(*r)