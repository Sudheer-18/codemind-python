r,c=map(int,input().split())
lst=[]
for i in range(r):
    lst.extend(list(map(int,input().split()))[:c:])
print(sum(lst))