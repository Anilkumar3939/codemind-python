def fun1(n):
    t=0
    for i in range(2,n):
        if(n%i==0):
            t=1
            return False
    if t==0:
        return True
def fun(n):
    x=n
    y=n
    while x!=0:
        if fun1(x):
            return abs(n-x)
        x-=1
        if fun1(y):
            return abs(n-y)
        y+=1

n=int(input())
print(fun(n))