x=input().lower()
y=input().lower()
a=x.split()
b=y.split()
c=0
for i in a:
    if i in b:
        c+=1
print(c)