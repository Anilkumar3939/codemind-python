import math
def fun(a):
    x=0
    if a==1 or a==0:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            x=1
            return False
    if x==0:
        return True


n=int(input())
l=list(map(int,input().split()))
a=min(l)
b=max(l)
a1=l.index(a)
a2=l.index(b)
if a1>a2:
    a1,a2=a2,a1
c=0
for i in range(a1,a2+1):
    if fun(l[i]):
        c+=1
print(c)