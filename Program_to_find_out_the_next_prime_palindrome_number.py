def fun1(n):
    t=0
    for i in range(2,n):
        if(n%i==0):
            t=1
            return False
    if t==0:
        return True
def fun(a):
    while 1:
        if fun1(a):
            s=str(a)
            if(s==s[::-1]):
                return a
        a+=1
    
a=int(input())
print(fun(a+1))