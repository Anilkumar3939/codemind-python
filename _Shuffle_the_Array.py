n=int(input())
l=list(map(int,input().split()))
b=int(input())
l1=[]
for i in range(n//2):
    l1.append(l[i])
    l1.append(l[b])
    b+=1
print(*l1)