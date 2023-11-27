def result(arr,n):
    for i in arr:
        if arr.count(i)>1:
            return i
    
    
    
n=int(input())
arr=list(map(int,input().split()))
print(result(arr,n))