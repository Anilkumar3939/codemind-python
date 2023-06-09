import itertools as t
a,b=map(int,input().split())
s=""
for i in range(1,a+1):
    s+=str(i)
f=list(s)
l=list(t.permutations(f,a))
r=1
for i in l:
    if r==b:
        print("".join(i))
    r+=1
    