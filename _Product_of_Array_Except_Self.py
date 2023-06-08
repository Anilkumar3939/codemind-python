l1=[]
n=int(input())
l=list(map(int,input().split()))
for i in l:
    s=1
    for j in l:
        if i!=j:
            s*=j
    print(s,end=" ")