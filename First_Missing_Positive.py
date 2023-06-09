n=int(input())
l=list(map(int,input().split()))
x=max(l)
t=0
for i in range(1,x+1):
    if i not in l:
        t=1
        print(i)
        break
if t==0:
    print(x+1)