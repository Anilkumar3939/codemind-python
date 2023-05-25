m=input()
a=0
l1=[]
for i in m:
    if i not in l1:
        l1.append(i)
    else:
        a=1
        break
if(a==1):
    print("False")
else:
    print("True")
        