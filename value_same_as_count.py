n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
        l2.append(l.count(i))
for i in range(len(l1)):
    if(l1[i]==l2[i]):
        c+=1
print(c)