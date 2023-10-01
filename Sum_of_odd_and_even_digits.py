n=int(input())
arr=list(map(int,input().split()))
s=0
ts=0
for i in range(0,len(arr)):
    if i==0:
        s+=arr[i]
    elif i%2==0:
        s+=arr[i]
    else:
        ts+=arr[i]
if s-ts==0:
    print("YES")
else:
    print("NO")
    