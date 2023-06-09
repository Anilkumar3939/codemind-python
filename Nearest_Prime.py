import math as m
def fun1(n):
    if n==1 or n==0:
        return True
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def fun(n):
    a=n
    b=n
    while 1:
        if fun1(a):
            print(a)
            break
        a-=1
        if fun1(b):
            print(b)
            break
        b+=1
n=int(input())
for i in range(n):
    x=int(input())
    fun(x)