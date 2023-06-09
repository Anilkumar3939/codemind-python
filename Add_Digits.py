n=str(input())
while len(n)!=1:
    l=[]
    for i in n:
        l.append(int(i))
    n=sum(l)
    n=str(n)
print(n)
    