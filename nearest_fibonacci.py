def fibno(s):
    if(s==0):
        return 0
    elif(s==1):
        return 1
    else:
        s=fibno(s-1)+fibno(s-2)
        return s
n=int(input())
s=0
fb=0
if n==0:
    print(0)
elif n==1:
    print(0)
else:
    while(fb<=n):
        fb=fibno(s)
        s=s+1
a=n-fibno(s-2)
b=fibno(s-1)-n
if(a<b):
    print(fibno(s-2))
elif(b<a):
    print(fibno(s-1))
else:
    print(fibno(s-2),fibno(s-1))