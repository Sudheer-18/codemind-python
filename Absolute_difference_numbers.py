n,m=map(int,input().split())
n=str(n)
el=[]
e1=''
e2=''
for i in range(0,m):
    e1+=n[i]
for i in range(1,m+1):
    e2+=n[-i]
e2=e2[::-1]
print(abs(int(e1)-int(e2)))