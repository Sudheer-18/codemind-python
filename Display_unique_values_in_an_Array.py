n=int(input())
arr=list(map(int,input().split()))
arr1=set(arr)
el=[]
for i in arr1:
    if arr.count(i)==1:
        el.append(i)
if len(el)==0:
    print(-1)
else:
    print(*el)