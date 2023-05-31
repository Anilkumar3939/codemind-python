n=int(input())
l=list(map(int,input().split()))
x=int(input())
l1=[]
l2=[]
l3=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
        l2.append(l.count(i))
for i in range(len(l1)):
    if(l2[i]==x):
        l3.append(l1[i])
        c=1
for i in l3:
    print(i,end=" ")
if c==0:
    print("-1")