l=input().lower()
n=l.split()
l1=[]
a=1
for i in n:
    for j in i:
            l1.append(j)
for i in l1:
    if l1.count(i)==1:
        print(i)
        a=0
        break
if a==1:
    print("-1")