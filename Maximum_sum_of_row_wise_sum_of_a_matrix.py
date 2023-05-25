a,b=map(int,input().split())
s=0
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(a):
    s1=0
    for j in range(b):
        s1+=l[i][j]
    if(s1>s):
        s=s1
print(s)