n=int(input())
l=list(map(int,input().split()))
d=dict()
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
s=0
s1=0
for i in d.keys():
    if d[i]>s:
        s=d[i]
        s1=i
    elif d[i]==s:
        if i<s1:
            s1=i
print(s1)