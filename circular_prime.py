import math
def fun(i):
    x=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            x=1
            return False
    if x==0:
        return True
a=int(input())
b=str(a)
c=0
if fun(a):
    c=1
if fun(int(b[::-1])):
    print("circular prime")
else:
    if c==1:
        print("prime but not a circular prime")
    else:
        print("not prime")

    
