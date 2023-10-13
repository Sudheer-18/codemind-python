n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
l=[]
for i in range(n):
    if (arr[i]<a or arr[i]>b):
        l.append(arr[i])
if(l==[]):
    print(-1);
else:
    for i in l:
        print(i,end=' ')