b=int(input())
m=b
n=b*b
s=0
while n:
    a=n%10
    s=s+a
    n=n//10
if(s==m):
    print("Neon Number")
else:
    print("Not Neon Number")