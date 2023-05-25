a,b=map(int,input().split())
s=0
l=[]
for i in range(a):
    l1=list(map(int,input().split()))
    l.append(l1)
for i in range(b):
    s1=0
    for j in range(a):
        s1+=l[j][i]
    if(s1>s):
        s=s1
print(s)