n=int(input())
count=n
s=0
l=len(str(n))
while n>0:
    a=n%10
    s=s+a**l
    n=n//10
    l=l-1
if(count==s):
    print("True")
else:
    print("False")