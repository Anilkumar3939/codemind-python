n=int(input())
l=list(map(int,input().split()))
l1=[]
s=0
c=0
for i in l:
    if i not in l1 and i==l.count(i):
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    a=sum(l1)/len(l1)
    print('%.2f'%a)