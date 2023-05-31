import math
def fun(i):
    x=0
    if i==1:
        return False
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            x=1
            return False
    if x==0:
        return True
a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    if fun(i):
        s+=1
print(s)
        