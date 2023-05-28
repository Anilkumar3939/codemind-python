n=list(input().split())
s1=0
s2=0
for i in range(len(n)):
    a=min(n[i])
    b=max(n[i])
    s1+=ord(a)
    s2+=ord(b)
print(abs(s1-s2))
        