n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
        l2.append(l.count(i))
x=len(l1)
for i in range(x):
    if l2[i]>=2:
        print(l1[i])
        
        
    