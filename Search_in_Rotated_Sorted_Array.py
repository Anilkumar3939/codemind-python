n=int(input())
l=list(map(int,input().split()))
t=int(input())
x=0
for i in l:
    if i==t:
        x=1
        print(l.index(t))
        break
if x==0:
    print(-1)