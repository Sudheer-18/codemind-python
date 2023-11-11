n=int(input())
arr=list(map(int,input().split()))
k=int(input())
arr1=set(arr)
arr1=list(arr1)
el=[]
for i in arr1:
    if(arr.count(i)==k):
        el.append(i)
if len(el)==0:
    print(-1)
else:
    print(*el)
