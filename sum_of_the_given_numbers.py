n=int(input())
l=list()
for i in range(n):
    m,o=map(int,input().split(" "))
    l.append(m+o)
for i in range(n):
    print(l[i])