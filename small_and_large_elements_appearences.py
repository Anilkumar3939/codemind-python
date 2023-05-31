n=input().split()
l1=[]
for i in n:
    for j in i:
        l1.append(j)
print(min(l1),l1.count(min(l1)),max(l1),l1.count(max(l1)))
