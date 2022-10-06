n=int(input())
count=0
i=2
while i<n:
    if(n%i==0):
        count=1
        break
    else:
        i=i+1
if(count==1):
    print("not a prime")
else:
    print("prime")