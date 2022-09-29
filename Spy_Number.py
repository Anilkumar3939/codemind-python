n=int(input())
s=0
m=1
while n:
    a=n%10
    s=s+a
    m=m*a
    n=n//10
if(s==m):
    print("Spy Number")
else:
    print("Not Spy Number")