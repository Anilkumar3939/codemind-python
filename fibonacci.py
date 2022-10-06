def fibno(s):
    if(s==0):
        return 0
    elif(s==1):
        return 1
    else:
        s=fibno(s-1)+fibno(s-2)
        return s
n=int(input())
for i in range(0,n,1):
    print(fibno(i),end=" ")
