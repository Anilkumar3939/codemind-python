a,b,c=map(int,input().split())
a1,b1,c1=map(int,input().split())
x=0
y=0
if a>a1:
    x+=1
elif a<a1:
    y+=1
if b>b1:
    x+=1
elif b<b1:
    y+=1
if c>c1:
    x+=1
elif c<c1:
    y+=1
print(x,y)