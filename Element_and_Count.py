import collections
n=int(input())
arr=list(map(int,input().split()))
d={}
d=collections.Counter(arr)
el=[]
for i,k in d.items():
    el.append(i)
    el.append(k)
print(*el)