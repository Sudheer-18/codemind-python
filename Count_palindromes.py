def is_palin(n):
    return n==n[::-1]
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if is_palin(str(i)):
        c+=1
print(c)
    