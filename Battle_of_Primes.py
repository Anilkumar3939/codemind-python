n1=int(input())
n2=int(input())
i=1
while i!=0:
    a=n1+n2+i
    j=2
    count=0
    while j<a:
        if(a%j==0):
            count=count+1
            break
        else:
            j=j+1
    if(count==1):
        i=i+1
    else:
        print(i)
        break