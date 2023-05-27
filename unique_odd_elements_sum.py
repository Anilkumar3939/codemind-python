n=int(input())
s=0
l=list(map(int,input().split()))
a=set(l)
l1=list(a)
for i in l1:
    if(i%2!=0):
        s+=i
print(s)