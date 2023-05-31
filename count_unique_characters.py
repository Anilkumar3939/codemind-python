l=input().lower()
n=l.split()
l1=[]
l2=[]
c=0
for i in n:
    for j in i:
            l1.append(j)
for i in l1:
    if i not in l2 and l1.count(i)==1:
        l2.append(i)
        c+=1
print(c)
