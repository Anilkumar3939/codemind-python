x=input().lower()
y=input().lower()
t=0
a=x.split()
b=y.split()
l1=[]
for i in b:
    if i in a:
        t=1
        print(i,end=" ")
if t==0:
    print("-1")