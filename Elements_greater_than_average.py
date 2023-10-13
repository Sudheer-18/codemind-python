n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)//n
c=0
for i in arr:
    if s<=i:
        c+=1
print(c)