def result(n, arr):
    for i in range(1, n+1):
        if i not in arr:
            return i

n = int(input())
arr = list(map(int, input().split()))
print(result(n, arr)) 
