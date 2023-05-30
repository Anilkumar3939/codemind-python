n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n):
    if i%2==0:
        if l[i]%2!=0:
            x=1
            print("False")
            break
            
        
if x==0:
    print("True")