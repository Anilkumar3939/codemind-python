import math
def fun(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
s=0
for i in range(1,n+1):
    if n%i==0:
        if fun(i)==False:
            s+=1
print(s)