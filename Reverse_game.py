def reverse(n):
    n=str(n)
    return n[::-1]
n=int(input())
arr=list(map(int,input().split()))
el=[]
for i in arr:
    print(int(reverse(i)),end=' ')