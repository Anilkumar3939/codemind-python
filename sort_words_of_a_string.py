n=list(input().split())
s="!@#$%^&*"
l1=[]
for i in n:
    a=list(i)
    l2=[]
    for j in range(len(a)):
        if a[j] not in s:
            l2.append(a[j])
            a[j]="*"
            
            
            
    l2.sort()
    x=0
    for k in range(len(a)):
        if(a[k]=="*"):
            a[k]=l2[x]
            x+=1
    l1.append(a)
l3=[]
for i in l1:
    z=''.join(i)
    l3.append(z)
print(*l3)