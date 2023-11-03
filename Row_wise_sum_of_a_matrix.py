r,c=map(int,input().split())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split()))[:c:])
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    print(s,end=' ')