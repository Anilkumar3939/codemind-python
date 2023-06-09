n=str(input())
s=len(n)
t1=0
t2=0
for i in n:
    if int(i)%2==0:
        t1+=1
    else:
        t2+=1
if t1==s:
    print("Even")
elif t2==s:
    print("Odd")
else:
    print("Mixed")
        