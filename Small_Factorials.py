def fun(x):
    s=1
    for i in range(1,x+1):
        s*=i
    print(s)
        

n=int(input())
for i in range(n):
    x=int(input())
    fun(x)