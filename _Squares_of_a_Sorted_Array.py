n=int(input())
arr=list(map(int,input().split()))
el=[]
for i in arr:
    el.append(i*i)
el.sort()
print(*el)