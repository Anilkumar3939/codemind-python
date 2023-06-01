n=input()
s="AEIOUaeiou"
l1=[]
for i in n:
    l1.append(i)
c=0
a=len(n)//2
x=-1
for j in range(a):
    if (n[j] in s and n[x]!=" " and n[x] not in s) or (n[j]!=" " and n[j] not in s and n[x] in s):
        c+=1
        x-=1
    else:
        x-=1
print(c)