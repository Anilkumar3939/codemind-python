a=int(input())
b=int(input())
def fun(s):
    s=str(s)
    if s==s[::-1]:
        return True
    return False
for i in range(a,b+1):
    if fun(i):
        print(i,end=" ")
    