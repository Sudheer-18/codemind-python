n = int(input())
arr = list(map(int, input().split()))
el = []
for i in arr:
    el.append(len(str(i)))
print(el.count(min(el)))
