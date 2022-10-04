def lcm(m,n):
    count=n
    while n:
        if(n%m==0):
            return n
        else:
            n=count+n
m,n=map(int,input().split(" "))
print(int(lcm(m,n)))
