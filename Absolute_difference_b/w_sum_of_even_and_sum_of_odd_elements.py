a=int(input())
b=list(map(int,input().split()))
s=0
s1=0
for i in range(0,len(b)):
    if b[i]%2==0:
        s=s+b[i]
    else:
        s1=s1+b[i]
print(abs(s-s1))