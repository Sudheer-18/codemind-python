n=int(input())
arr=list(map(int,input().split()))
mid=n//2
s=s1=0
for i in range(mid):
    s+=arr[i]
for j in range(mid,n):
    s1+=arr[j]
print(s1-s)
    