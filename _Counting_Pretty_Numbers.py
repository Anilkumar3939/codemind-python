def pr(m,n):
    c=0
    for i in range(m,n+1):
        if(i%10==2 or i%10==9 or i%10==3):
            c=c+1
    print(c)
n=int(input())
for i in range(0,n):
    m,n=map(int,input().split())
    pr(m,n)