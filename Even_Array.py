n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
    if i%2!=0:
        x=1
        print("False")
        break
if x==0:
    print("True")