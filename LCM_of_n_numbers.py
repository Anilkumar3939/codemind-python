n=int(input())
l=list(map(int,input().split()))
a=max(l)
x=a
while 1:
    t=0
    for i in l:
        if x%i!=0:
            t=1
            break
    if t==0:
        print(x)
        break
    else:
        x+=a

    