n=int(input())
while n>9:
    s=0
    while n>0:
        a=n%10
        s=s+a*a
        n=n//10
    if(s<9):
        if(s==1):
            print("True")
            break
        else:
            print("False")
            break
    else:
        n=s
