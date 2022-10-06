n=int(input())
i=2
count1=0
while i<=n:
    if(n%i==0):
        j=2
        count=0
        while j<i:
            if(i%j==0):
                count=1
                break
            else:
                j=j+1
        if(count==1):
            count1=count1+1
    i=i+1
print(count1+1)
            
        
            

