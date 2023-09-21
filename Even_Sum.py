a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(0,len(b)):
    if b[i]%2==0:
        s=s+b[i]
print(s)