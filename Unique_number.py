n=int(input())
len1=len(str(n))
l=list()
while n>0:
    e=n%10
    l.append(e)
    n=n//10
i=0
j=0
count=0
for i in range(i,len1,1):
    for j in range(i+1,len1,1):
        if(l[i]==l[j]):
            count=1
            break
if(count==1):
    print("Not Unique Number")
else:
    print("Unique Number")