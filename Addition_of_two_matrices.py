n=int(input())
l=[]
l1=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    l1.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        x=l[i][j]+l1[i][j]
        print(x,end=' ')
    print()