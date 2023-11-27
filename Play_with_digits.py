n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    while i!=0:
        r=i%10
        i//=10
        s+=r
print(s)
        