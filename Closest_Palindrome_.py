n=int(input())
x=n-1
s=n+1
l=[]
while x!=0:
    a=str(x)
    if(str(x)==a[::-1]):
        l.append(x)
        break
    else:
        x-=1
while s!=0:
    a=str(s)
    if(str(s)==a[::-1]):
        l.append(s)
        break
    else:
        s+=1
b=l[1]-n
a=n-l[0]
if(a<b):
    print(l[0])
elif(a>b):
    print(l[1])
else:
    print(l[0],l[1])
    