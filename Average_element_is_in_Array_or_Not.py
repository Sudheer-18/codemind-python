a=int(input())
b=list(map(int,input().split()))
s=0
flag=0
for i in b:
    s=s+i
avg=s//7
for i in range(0,len(b)):
    if(avg==b[i]):
        flag=1
        break
if flag==1:
    print("True")
else:
    print("False")
    