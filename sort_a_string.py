n=list(input())
s=" ,!@#$%^&*()"
l1=[]
for i in range(len(n)):
    if n[i] not in s:
        l1.append(n[i])
        n[i]="*"
l1.sort()
x=0
for i in range(len(n)):
    if(n[i]=="*"):
        n[i]=l1[x]
        x+=1
x1="".join(n)
print(x1)
    
        