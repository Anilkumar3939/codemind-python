x=input().lower()
a=x.split()
l1=[]
for j in a[0]:
    t=0
    for k in range(1,len(a)):
        if j not in a[k]:
            t=1
    if t==0:
        l1.append(j)
print(len(l1))