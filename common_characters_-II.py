x=input().lower()
y=input().lower()
l11=[]
l2=[]
a=x.split()
b=y.split()
l1=[]
for i in a:
    for j in i:
        l1.append(j)
for i in b:
    for j in i:
        l2.append(j)
for i in l1:
    if i in l2:
        l11.append(i)
for i in l2:
    if i in l1:
        l11.append(i)
l22=set(l11)
l11=list(l22)
l11.sort()
print(len(l11))