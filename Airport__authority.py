n=int(input())
l=[]
m=0
for i in range(n):
    x=int(input())
    l.append(x)
w=int(input())
for i in l:
    if i<=w:
        m+=1
    else:
        m+=2
print(m)