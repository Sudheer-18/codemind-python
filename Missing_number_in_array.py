def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    result=missing_number(arr,n)
    print(result)