n=int(input())
k=n
f=0
for i in range(1,n+1):
    for j in range(1,k):
        print(" ",end="")
    for l in range(f+i):
        print(i,end="")
    k=k-1
    f=f+1
    print()