n=int(input())
l=list(map(int,input().split()))
a=min(l)
s=[]
for i in range(1,a+1):
    b=0
    for j in l:
        if j%i!=0:
            b=1
            break
    if b==0:
        s.append(i)
print(max(s))
            
        