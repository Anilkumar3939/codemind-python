n=input().split()
l=n[-1]
m=min(l)
if m.lower() in l:
    print(m.lower())
else:
    print(m)