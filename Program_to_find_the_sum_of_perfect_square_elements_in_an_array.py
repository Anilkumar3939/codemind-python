n=int(input())
sum1=0
l=list(map(int,input().split()))
for i in l:
    for j in range(1,i+1,1):
        if(i==j*j):
            sum1=sum1+i
            break
print(sum1)