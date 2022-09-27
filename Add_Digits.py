n=int(input())
sum=0
cond=True
while cond:
    while n>0:
        sum=sum+n%10
        n=n//10
    n=sum
    sum=0
    cond=n>10
print(n)