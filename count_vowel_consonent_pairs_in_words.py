n=input().split()
s="AEIOUaeiou"
c=0
for i in n:
    a=len(i)//2
    x=-1
    for j in range(a):
        if (i[j] in s and i[x] not in s) or (i[j] not in s and i[x] in s):
            c+=1
            x-=1
        else:
            x-=1
print(c)
    