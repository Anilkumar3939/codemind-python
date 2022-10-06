n=int(input())
a=0
b=1
count=0
for i in range(1,n+1):
    s=a+b
    a,b=b,a
    if(n==s):
        count=1
        break
    else:
        b=s

if(count==1):
    print("True")
else:
    print("False")