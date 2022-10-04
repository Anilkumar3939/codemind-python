m=int(input())
n=int(input())
sum1=0
sum2=0
j=1
i=1
while i<m:
    if(m%i==0):
        sum1=sum1+i
    i=i+1
while j<n:
    if(n%j==0):
        sum2=sum2+j
    j=j+1
if(sum1==n and sum2==m):
    print("Amicable")
else:
    print("Not Amicable")