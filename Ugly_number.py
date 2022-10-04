n=int(input())
count=0
while n!=1:
    if(n%2==0):
        n=n/2
    elif(n%3==0):
        n=n/3
    elif(n%5==0):
        n=n/5
    else:
        count=1
        break
if(count==1):
    print("Not Ugly Number")
else:
    print("Ugly Number")