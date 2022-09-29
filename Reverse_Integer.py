num=int(input())
m=num
s=0
while num:
    if(num<0):
        num=num*-1
    a=num%10
    s=s*10+a
    num=num//10
if(m>0):
    print(s)
else:
    print("-"+str(s))