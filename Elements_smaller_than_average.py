n = int(input())
arr = list(map(int, input().split()))
avg = sum(arr) / n
count = 0

for i in arr:
    if i <= avg:
        count += 1

print(count)
