import itertools as t
n=int(input())
m=int(input())
l=[]
l1=[]
for i in range(n,m+1):
    l.append(i)
for i in range(1,3):
   a=t.combinations(l,i)
   l1=l1+(list(a))
c=0
for i in l1:
    if sum(i)%2!=0:
        c=c+1
print(c)