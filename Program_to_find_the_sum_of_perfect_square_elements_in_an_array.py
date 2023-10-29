def Perfect_Square(n):
    k=int(n**0.5)
    return n==(k*k)
    
n=int(input())
arr=list(map(int,input().split()))
arr=set(arr)
s=0
for i in arr:
    if Perfect_Square(i):
        s+=i
print(s)