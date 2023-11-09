n=int(input())
arr=list(map(int,input().split()))
k=int(input())
lst=[]
arr1=set(arr)
for i in arr1:
    if arr.count(i)==k:
        lst.append(i)
if len(lst)!=0:
    print(*lst)
else:
    print(-1)
        