n=int(input())
l=list(map(int,input().split()))
a=len(l)//2
l1=l[a::]
print(*(l1[::-1]+l[0:a]))