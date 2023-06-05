n=int(input())
l=list(map(int,input().split()))
l1=[]
x=0
y=0
for i in l:
    
    if i%2==0:
        x+=1
    else:
        y+=1
        
print(x,y)        