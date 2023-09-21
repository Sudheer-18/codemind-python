a=int(input())
b=list(map(int,input().split()))
for i in range(0,len(b)):
    min1=b[0]
    if(min1>b[i]):
        min1=b[i]
print(min1)