def fun1(n):
    t=0
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            t=1
            return False
    if t==0:
        return True
def fun(n):
    if not fun1(n):
        return "Not Mega Prime"
    for i in str(n):
        if not fun1(int(i)):
            return "Not Mega Prime"
    else:
        return "Mega Prime"
            

n=int(input())
print(fun(n))