l=input().lower()
n=l.split()
l1=[]
l2=[]
for i in n:
    for j in i:
            l1.append(j)
for i in l1:
    if i not in l2:
        l2.append(i)
l2.sort()
print("".join(l2))