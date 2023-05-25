n=input().lower()
s=0
l=n.split(" ")
for i in l:
    if(i==i[::-1]):
        s+=1
print(s)