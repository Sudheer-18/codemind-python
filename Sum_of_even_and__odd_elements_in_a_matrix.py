r,c=map(int,input().split())
lst=[]
for i in range(r):
    lst.append(list(map(int,input().split()))[:c:])
e=o=0
for i in range(r):
    for j in range(c):
        if(lst[i][j]%2==0):
            e+=lst[i][j]
        else:
            o+=lst[i][j]
print(e,o)
    