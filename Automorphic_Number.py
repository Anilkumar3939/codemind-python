n=int(input())
l=len(str(n))
s=n*n
l2=len(str(s))
d=0
c=0
while l2>l:
    a=s%10
    d=d*10+a
    s=s//10
    l2=l2-1
while d:
    b=d%10
    c=c*10+b
    d=d//10
if(c==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")