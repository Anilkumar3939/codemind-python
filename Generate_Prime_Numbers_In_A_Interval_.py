import math as m
def fun(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i):
        print(i)