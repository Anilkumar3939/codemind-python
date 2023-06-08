n=input().lower()
s="aeiou"
s1=""
if n[0] in s:
    s1="V"
else:
    s1="C"
for i in n:
    if i in s:
        if s1[-1]=="C":
            s1+="V"
    else:
        if s1[-1]=="V":
            s1+="C"
print(s1)
    
