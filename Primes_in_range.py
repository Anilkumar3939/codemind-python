import math as m
a=int(input())
b=int(input())
if a>b:
    a,b=b,a
c=0
def fun(i):
    x=0
    if i==1 or i==0:
        return False
    for j in range(2,int(m.sqrt(i))+1):
        if i%j==0:
            x=1
            return False
    if x==0:
        return True
for i in range(a,b+1):
    if fun(i):
        c+=1
print(c)