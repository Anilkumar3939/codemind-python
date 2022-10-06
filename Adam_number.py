n=int(input())
s=0
d=0
square1=n*n
while n>0:
    a=n%10
    s=s*10+a
    n=n//10
square2=s*s
while square2>0:
    b=square2%10
    d=d*10+b
    square2=square2//10
if(square1==d):
    print("True")
else:
    print("False")